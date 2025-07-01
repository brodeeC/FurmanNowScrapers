import json
import sqlite3
import polyline

def handle_colors(colors):
    color_dict = {
        'yellow': 0,
        'green': 0,
        'blue': 0,
        'silver': 0,
        'orange': 0,
        'purple': 0,
        'lightPurple': 0,
        'public_col': 0
    }

    if ',' in colors:
        colors = colors.split(',')
    else:
        colors = colors.split(' ')
    
    for color in colors:
        color_dict[color] = 1
    
    return color_dict

def extract_data(file_path):
    with open(file_path, 'r') as f:
        # Load data
        data = json.load(f)

        # Iterate over features
        for feature in data['features']:

            # Get coordinates
            coords = feature['geometry']['coordinates']

            # Flip to lat, lng for polyline.encode
            coords_latlng = [[lat, lng] for lng, lat in coords[0]]
            boundry = polyline.encode(coords_latlng)

            # Get properties
            properties = feature['properties']
            _id = feature['id']
            zoneName = properties['Name']

            # Determine active colors
            colors = properties['colors']
            color_dict = handle_colors(colors)
            
            # Connect to database and insert data
            conn = sqlite3.connect('backend/database/FUNow.db')
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO parkingZones (
                    id, zoneName, boundry, yellow, green, blue, silver, orange, purple, lightPurple, public_col
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                _id,
                zoneName,
                boundry,
                color_dict['yellow'],
                color_dict['green'],
                color_dict['blue'],
                color_dict['silver'],
                color_dict['orange'],
                color_dict['purple'],
                color_dict['lightPurple'],
                color_dict['public_col'],
            ))

            conn.commit()
            conn.close()

def main():
    extract_data('backend/aux/parkingMap.json')

if __name__ == '__main__':
    main()