import sqlite3

def update_image_links(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
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

# Currently contains 49,980 lines in buildingHours.
def main():
    update_image_links('backend/database/FUNow.db')


    conn = sqlite3.connect('backend/database/FUNow.db')
    cursor = conn.cursor()

    # cursor.execute("SELECT buildingID, day, Start, End FROM buildingHours")
    # buildings = cursor.fetchall()
    # print("Buildings in database:")
    # for buildingID, day, Start, End in buildings:
    #     print(f"ID: {buildingID}, Day: {day}, Start: {Start}, End: {End}")

    cursor.execute("SELECT COUNT(*) FROM buildingHours")
    print(cursor.fetchone())
    cursor.execute("""
        SELECT buildingID, COUNT(*) AS num_entries
        FROM buildingHours
        GROUP BY buildingID
        ORDER BY num_entries DESC;
    """)
    tuples = cursor.fetchall()
    for buildings in tuples:
        building_id, entries = buildings[0], buildings[1]
        cursor.execute(f"SELECT name FROM buildingLocations WHERE buildingID = {building_id};")
        res = cursor.fetchone()
        name = res[0] if res else 'Unknown'
        print(f'Name: {name} - entries: {entries}')
    # cursor.execute("SELECT * FROM clps")
    # res = cursor.fetchall()
    # for result in res:
    #     print(result)

    conn.close()

if __name__ == '__main__':
    main()