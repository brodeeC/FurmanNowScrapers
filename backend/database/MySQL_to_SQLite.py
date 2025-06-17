import re

# Exucution: python3 backend/database/MySQL_to_SQLite.py backend/database/FUNOW.sql -o backend/database/output.sql -d backend/database/FUNow.db

def convert_mysql_to_sqlite(mysql_sql: str) -> str:
    """
    Converts MySQL SQL to SQLite-compatible SQL
    """
    # Remove MySQL-specific statements
    sqlite_sql = re.sub(r'^SET.*?;', '', mysql_sql, flags=re.MULTILINE | re.IGNORECASE)
    
    # Remove engine and charset specifications
    sqlite_sql = re.sub(r'\s*ENGINE\s*=\s*\w+', '', sqlite_sql, flags=re.IGNORECASE)
    sqlite_sql = re.sub(r'\s*DEFAULT\s+CHARSET\s*=\s*\w+', '', sqlite_sql, flags=re.IGNORECASE)
    sqlite_sql = re.sub(r'\s*AUTO_INCREMENT\s*=\s*\d+', '', sqlite_sql, flags=re.IGNORECASE)
    mysql_sql = re.sub(r'^\s*DELIMITER\s+.*$', '', mysql_sql, flags=re.MULTILINE|re.IGNORECASE)
    
    # Convert data types
    type_mappings = [
        (r'\btinyint\(\d+\)', 'INTEGER'),
        (r'\bsmallint\(\d+\)', 'INTEGER'),
        (r'\bmediumint\(\d+\)', 'INTEGER'),
        (r'\bint\(\d+\)', 'INTEGER'),
        (r'\bbigint\(\d+\)', 'INTEGER'),
        (r'\bdatetime\b', 'TEXT'),
        (r'\btimestamp\b', 'TEXT'),
        (r'\bdouble\b', 'REAL'),
        (r'\bfloat\b', 'REAL'),
        (r'\bdecimal\(.*?\)', 'REAL'),
        (r'\bvarchar\(\d+\)', 'TEXT'),
        (r'\bchar\(\d+\)', 'TEXT'),
        (r'\btext\b', 'TEXT'),
        (r'\blongtext\b', 'TEXT'),
        (r'\bmediumtext\b', 'TEXT'),
        (r'\benum\((.*?)\)', lambda m: f'TEXT CHECK({m.group(1).split(",")[0].strip()} IN ({m.group(1)}))')
    ]
    
    for pattern, replacement in type_mappings:
        sqlite_sql = re.sub(pattern, replacement, sqlite_sql, flags=re.IGNORECASE)
    
    # Remove backticks
    sqlite_sql = sqlite_sql.replace('`', '')
    
    # Handle AUTO_INCREMENT
    sqlite_sql = re.sub(
        r'(\s+)(\w+)\s+(?:INTEGER|INT|BIGINT).*?AUTO_INCREMENT',
        r'\1\2 INTEGER PRIMARY KEY AUTOINCREMENT',
        sqlite_sql,
        flags=re.IGNORECASE
    )
    
    # Remove unsigned modifiers
    sqlite_sql = re.sub(r'\sunsigned', '', sqlite_sql, flags=re.IGNORECASE)
    
    # Remove COMMENT clauses
    sqlite_sql = re.sub(r'\sCOMMENT\s+\'.*?\'', '', sqlite_sql, flags=re.IGNORECASE)

    def process_triggers(sql_content):
        # Pattern to match entire trigger blocks including DELIMITER wrappers
        trigger_pattern = r'DELIMITER \$\$(.*?)\$\$\s*DELIMITER ;'
        triggers = re.findall(trigger_pattern, sql_content, flags=re.DOTALL)
        
        converted_triggers = []
        for trigger in triggers:
            # Clean each trigger block
            trigger = trigger.strip()
            if not trigger:
                continue
                
            # Convert to SQLite format
            trigger = re.sub(r'^CREATE TRIGGER', 'CREATE TRIGGER', trigger)
            trigger = re.sub(r'FOR EACH ROW\s*', '', trigger)
            trigger = re.sub(r'^\s*BEGIN\s*', 'BEGIN\n    ', trigger)
            trigger = re.sub(r'^\s*END\s*\$\$', 'END;', trigger)
            
            # Ensure proper semicolons
            if not trigger.endswith(';'):
                trigger += ';'
                
            converted_triggers.append(trigger)
        
        # Join with double newlines between triggers
        return '\n\n'.join(converted_triggers)

    # Extract and convert all triggers first
    converted_triggers = process_triggers(mysql_sql)
    
    # Remove all original trigger blocks from SQL
    sqlite_sql = re.sub(r'DELIMITER \$\$.*?\$\$\s*DELIMITER ;', '', sqlite_sql, flags=re.DOTALL)
    
    # Add the converted triggers at the end of the file
    if converted_triggers:
        sqlite_sql = sqlite_sql.strip() + '\n\n' + converted_triggers
    
    # Convert MySQL triggers to SQLite format
    def convert_trigger(match):
        trigger_name = match.group(1).strip().replace(' ', '_')
        timing = match.group(2).strip()
        event = match.group(3).strip()
        table = match.group(4).strip()
        body = match.group(5).strip()
        
        # Clean up the body
        body = re.sub(r'^\$\$|\$\$$', '', body)
        body = body.strip()
        
        # Ensure body ends with semicolon
        if body and not body.endswith(';'):
            body += ';'
            
        # Format for SQLite with proper newlines
        return f"""CREATE TRIGGER {trigger_name}
{timing} {event} ON {table}
BEGIN
    {body}
END;
"""

    # Apply trigger conversion with improved regex
    sqlite_sql = re.sub(
        r'CREATE\s+TRIGGER\s+(.*?)\s+(BEFORE|AFTER)\s+(INSERT|UPDATE|DELETE)\s+ON\s+(.*?)\s+FOR\s+EACH\s+ROW\s+([\s\S]*?)(?=\$\$|DELIMITER|CREATE TRIGGER|\Z)',
        convert_trigger,
        sqlite_sql,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # Remove MySQL-specific index types
    sqlite_sql = re.sub(r'\sUSING\s+\w+', '', sqlite_sql, flags=re.IGNORECASE)
    
    # Clean up whitespace
    sqlite_sql = re.sub(r'\n\s*\n', '\n\n', sqlite_sql)
    
    return sqlite_sql.strip()
        

def execute_sqlite_script(db_path: str, sql_script: str) -> None:
    import sqlite3
    from contextlib import closing
    
    with closing(sqlite3.connect(db_path)) as conn:
        cursor = conn.cursor()
        
        # First try to execute as complete script
        try:
            cursor.executescript(sql_script)
            conn.commit()
            return
        except sqlite3.Error as e:
            print(f"Script execution failed, trying statement-by-statement: {e}")
        
        # Fallback to statement-by-statement execution
        statements = []
        current_statement = ""
        in_trigger = False
        
        for line in sql_script.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            current_statement += line + "\n"
            
            # Detect trigger blocks
            if line.startswith("CREATE TRIGGER"):
                in_trigger = True
            elif in_trigger and line.startswith("END;"):
                statements.append(current_statement)
                current_statement = ""
                in_trigger = False
            elif not in_trigger and line.endswith(";"):
                statements.append(current_statement)
                current_statement = ""
        
        # Execute all statements
        for stmt in statements:
            try:
                cursor.execute(stmt)
            except sqlite3.Error as e:
                print(f"Error executing: {e}")
                print(f"Statement: {stmt[:200]}...")
                raise
        
        conn.commit()

def process_sql_file(input_file: str, output_file: str = None, db_path: str = None) -> None:
    """
    Processes SQL file and optionally saves output and/or executes on database
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        mysql_sql = f.read()
    
    sqlite_sql = convert_mysql_to_sqlite(mysql_sql)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(sqlite_sql)
        print(f"Converted SQL saved to {output_file}")
    
    if db_path:
        print("Executing on SQLite database...")
        execute_sqlite_script(db_path, sqlite_sql)
        print("Execution completed successfully")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert MySQL SQL to SQLite')
    parser.add_argument('input_file', help='Input MySQL SQL file')
    parser.add_argument('--output', '-o', help='Output SQLite SQL file')
    parser.add_argument('--db', '-d', help='SQLite database file to execute on')
    
    args = parser.parse_args()
    
    process_sql_file(
        input_file=args.input_file,
        output_file=args.output,
        db_path=args.db
    )