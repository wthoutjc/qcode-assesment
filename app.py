import os
from decouple import config
from src.init_app import init_app

# Database
from src.models.models import db

# Seed data
from src.load_data import load_data

time_zone = config('TZ')
os.environ['TZ'] = time_zone

app = init_app()

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        load_data()
    app.run(debug=True, host="0.0.0.0", port=5000)