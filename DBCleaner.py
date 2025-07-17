import os
import psycopg2
from psycopg2 import sql

def update_image_links():
    database_url = os.environ['DATABASE_URL']
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()
    
    try:
        # Fetch all records from newsContent table
        cursor.execute("""
            SELECT id, imagelink FROM "newsContent" 
            WHERE imagelink IS NOT NULL
        """)
        rows = cursor.fetchall()
        
        updates = []
        
        for row in rows:
            rowid, image_link = row
            if image_link and '/articleImages' in image_link:
                pos = image_link.find('/articleImages')
                new_link = image_link[pos:]
                
                if new_link != image_link:
                    updates.append((new_link, rowid))
        
        if updates:
            query = sql.SQL("""
                UPDATE "newsContent" 
                SET imagelink = %s 
                WHERE id = %s
            """)
            cursor.executemany(query, updates)
            conn.commit()
            print(f"Updated {len(updates)} image links")
        else:
            print("No image links needed updating")
            
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        conn.close()

def remove_dup_stops():
    database_url = os.environ['DATABASE_URL']
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT "stopName", COUNT(*) as count
            FROM stop_with_distance
            GROUP BY "stopName"
            HAVING COUNT(*) > 1
            ORDER BY "stopName" NULLS FIRST
        """)
        duplicate_stops = cursor.fetchall()

        if not duplicate_stops:
            print("No duplicate stops found.")
            return

        total_deleted = 0

        for stop in duplicate_stops:
            stop_name, count = stop
            print(f"\nProcessing {'unnamed stops' if stop_name is None else stop_name} ({count} entries)")

            if stop_name is None:
                cursor.execute("""
                    SELECT "lineID", "stopOrderID"
                    FROM stop_with_distance
                    WHERE "stopName" IS NULL
                """)
            else:
                cursor.execute("""
                    SELECT "lineID", "stopOrderID"
                    FROM stop_with_distance
                    WHERE "stopName" = %s
                """, (stop_name,))
            
            rows = cursor.fetchall()

            # Find the entry with smallest lineID and stopOrderID to keep
            smallest = min(rows, key=lambda x: (x[0], x[1]))
            print(f"Keeping: lineID={smallest[0]}, stopOrderID={smallest[1]}")

            # Delete all other entries for this stop name
            if stop_name is None:
                cursor.execute("""
                    DELETE FROM "stopsTable"
                    WHERE stopName IS NULL
                    AND ("lineID" != %s OR "stopOrderID" != %s)
                """, (smallest[0], smallest[1]))
            else:
                cursor.execute("""
                    DELETE FROM "stopsTable"
                    WHERE stopName = %s
                    AND ("lineID" != %s OR "stopOrderID" != %s)
                """, (stop_name, smallest[0], smallest[1]))

            deleted_count = cursor.rowcount
            total_deleted += deleted_count
            print(f"Deleted {deleted_count} duplicate(s)")

        conn.commit()
        print(f"\nTotal duplicates deleted: {total_deleted}")

    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
        raise
    finally:
        conn.close()

def main():
    update_image_links()
    remove_dup_stops()

if __name__ == '__main__':
    main()