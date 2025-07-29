"""
Initializes sqlalchemy 'Session'
"""

from backend.app.routes import create_app, db
from sqlalchemy import text  # Required for raw SQL
from sqlalchemy import inspect

def verify_db_connection():
    """Verify connection to existing database without modifications"""
    app = create_app()
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1")).scalar()
            print("Database connection successful!")
            
            engine = db.get_engine()
            
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            print(f"Found tables: {tables}")
            
            required_tables = {
                'buildingHours',
                'buildingLocations',
                'shuttles',
                'vehicleNames',
                'weather',
                'images',
                'vehicleLocations',
                'athletics',
                'clp',
                'contacts',
                'DHmenu',
                'healthSafety',
                'importantDate',
                'importantLinks',
                'newsContent',
                'newsPublishers',
                'shuttleStops',
                "BusStops",
                "FU20_RestaurantHours",
                "foodService",
                "parkingResources",
                "parkingZones"
            }
            missing_tables = required_tables - set(tables)
            if missing_tables:
                print(f"Missing tables: {missing_tables}")
            else:
                print("All required tables present")
                
            return True
            
        except Exception as e:
            print(f"Database verification failed: {str(e)}")
            return False

if __name__ == '__main__':
    verify_db_connection()