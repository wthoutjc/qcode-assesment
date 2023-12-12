from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

class Services(db.Model):
    id_service = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    schedules = db.relationship('Schedules', backref='service', lazy=True)

    def serialize(self):
        return {
            'id': self.id_service,
            'name': self.name,
            'description': self.description,
            'schedules': [schedule.serialize() for schedule in self.schedules]
        }

class Schedules(db.Model):
    id_schedule = db.Column(db.Integer, primary_key=True)
    id_service = db.Column(db.Integer, db.ForeignKey('services.id_service'), nullable=False)
    day = db.Column(db.String(10), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id_schedule,
            'id_service': self.id_service,
            'day': self.day,
            'start_time': str(self.start_time),
            'duration': self.duration
        }