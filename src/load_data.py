import json
import random
import datetime

# Models
from src.models.models import db, Services, Schedules

def load_data():
    # Cargar y guardar los servicios
    with open('seed-services.json') as f:
        services_data = json.load(f)
        services = []
        for item in services_data:
            service = Services(name=item['name'], description=item['description'])
            db.session.add(service)
            services.append(service)
        db.session.commit()

    # Cargar y guardar las citas
    with open('seed-schedules.json') as f:
        schedules_data = json.load(f)
        for item in schedules_data:
            start_time = datetime.datetime.strptime(item['Hour'], '%H:%M').time()
            service = random.choice(services)  # Choose a random service
            schedule = Schedules(id_service=service.id_service, day=item['Day'], start_time=start_time, duration=int(item['Duration']))
            db.session.add(schedule)
        db.session.commit()