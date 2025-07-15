import sqlite3
import os
import psycopg2

def update_image_links(db_path):
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()
    database_url = os.environ['DATABASE_URL']

    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()
    
    try:
        # Fetch all records from newsContent table
        cursor.execute("SELECT rowid, imagelink FROM newsContent WHERE imagelink IS NOT NULL")
        rows = cursor.fetchall()
        
        updates = []
        
        for row in rows:
            rowid, image_link = row
            if image_link and '/articleImages' in image_link:
                # Find the position of '/articleImages'
                pos = image_link.find('/articleImages')
                # Keep everything from '/articleImages' onward
                new_link = '' + image_link[pos:]
                
                # Only update if the link actually changed
                if new_link != image_link:
                    updates.append((new_link, rowid))
        
        # Update all changed records in a single transaction
        if updates:
            cursor.executemany(
                "UPDATE newsContent SET imagelink = ? WHERE rowid = ?",
                updates
            )
            conn.commit()
            print(f"Updated {len(updates)} image links")
        else:
            print("No image links needed updating")
            
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        conn.close()

def remove_dup_stops(db_path):
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    database_url = os.environ['DATABASE_URL']

    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()

    stop_name = '600 Block Rutherford Rd'

    cursor.execute("""
        SELECT lineID, stopOrderID
        FROM stop_with_distance
        WHERE stopName=?
    """, (stop_name,))
    rows = cursor.fetchall()

    if len(rows) <= 1:
        print("Nothing to remove: only one or zero entries.")
    else:
        smallest = min(rows, key=lambda x: (x[0], x[1]))
        print(f"Keeping: lineID={smallest[0]}, stopOrderID={smallest[1]}")

        cursor.execute(f"""
            DELETE FROM stopsTable
            WHERE stopName=?
            AND (lineID != ? OR stopOrderID != ?)
        """, (stop_name, smallest[0], smallest[1]))

        print(f"Deleted {cursor.rowcount} duplicate(s).")

    conn.commit()

    print(cursor.fetchall())

    conn.close()

def main():
    update_image_links('backend/database/FUNow.db')
    remove_dup_stops('backend/database/FUNow.db')

if __name__ == '__main__':
    main()