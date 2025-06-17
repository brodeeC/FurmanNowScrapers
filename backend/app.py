"""
Starts Flask app.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # TODO: Change to just app.run() when it goes on the server
    app.run(host="0.0.0.0", port=5050, debug=True) 