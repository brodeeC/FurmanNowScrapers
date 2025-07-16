import json
import sqlite3
import polyline
import psycopg2
import os

def handle_colors(colors):
    color_dict = {
        'yellow': False,
        'green': False,
        'blue': False,
        'silver': False,
        'orange': False,
        'purple': False,
        'lightPurple': False,
        'public_col': False
    }

    if ',' in colors:
        colors = colors.split(',')
    else:
        colors = colors.split(' ')
    
    for color in colors:
        color_dict[color] = True
    
    return color_dict

def extract_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

        for feature in data['features']:

            coords = feature['geometry']['coordinates']

            # Flip to lat, lng for polyline.encode
            coords_latlng = [[lat, lng] for lng, lat in coords[0]]
            boundry = polyline.encode(coords_latlng)

            properties = feature['properties']
            _id = feature['id']
            zoneName = properties['Name']

            colors = properties['colors']
            color_dict = handle_colors(colors)
            
            database_url = os.environ['DATABASE_URL']

            conn = psycopg2.connect(database_url)
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