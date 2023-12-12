import datetime

# Model
from src.models.models import Schedules, db
from sqlalchemy.exc import IntegrityError

# Utils
from src.utils.add_to_time import add_to_time
from src.utils.str_to_time import str_to_time

class ScheduleController:
    @staticmethod
    def create_schedule(data: dict):
        """
        This is the schedule controller that creates a schedule.
        ---
        parameters:
        - data (dict): The data of the schedule.
        responses:
        200:
            description: The schedule was successfully created.
        400:
            description: The schedule was not successfully created.
        """
        start_time = datetime.datetime.strptime(data['start_time'], '%H:%M:%S').time()
        new_schedule = Schedules(day=data['day'], start_time=start_time, duration=data['duration'], id_service=data['id_service'])
        db.session.add(new_schedule)
        try:
            db.session.commit()
            return { 'message': 'Schedule created successfully' }, 200
        except IntegrityError:
            db.session.rollback()
            return { 'message': 'Schedule already exists' }, 400

    @staticmethod
    def get_schedules():
        """
        This is the schedule controller that gets all schedules.
        ---
        parameters:
        - None
        responses:
        200:
            description: The schedules were successfully retrieved.
        400:
            description: The schedules were not successfully retrieved.
        """
        schedules = Schedules.query.all()
        return { 'schedules': [schedule.serialize() for schedule in schedules] }, 200

    @staticmethod
    def get_schedule_by_id(id_schedule: int):
        """
        This is the schedule controller that gets a schedule by id.
        ---
        parameters:
        - id_schedule (int): The id of the schedule.
        responses:
        200:
            description: The schedule was successfully retrieved.
        404:
            description: The schedule was not found.
        """
        schedule = Schedules.query.get(id_schedule)
        if schedule:
            return { 'schedule': schedule.serialize() }, 200
        return { 'message': 'Schedule not found' }, 404

    @staticmethod
    def get_schedule_by_day(day: str):
        """
        This is the schedule controller that gets a schedule by day.
        ---
        parameters:
        - day (string): The day of the schedule.
        responses:
        200:
            description: The schedule was successfully retrieved.
        404:
            description: The schedule was not found.
        """
        schedule = Schedules.query.filter_by(day=day).all()
        if schedule:
            return { 'schedule': [schedule.serialize() for schedule in schedule] }, 200
        return { 'message': 'Schedule not found' }, 404

    @staticmethod
    def update_schedule(id_schedule: int, data: dict):
        """
        This is the schedule controller that updates a schedule.
        ---
        parameters:
        - id_schedule (int): The id of the schedule.
        - data (dict): The data of the schedule.
        responses:
        200:
            description: The schedule was successfully updated.
        404:
            description: The schedule was not found.
        """
        schedule = Schedules.query.get(id_schedule)
        if schedule:
            schedule.day = data['day']
            schedule.start_time = datetime.datetime.strptime(data['start_time'], '%H:%M:%S').time()
            schedule.duration = data['duration']
            db.session.commit()
            return { 'message': 'Schedule updated successfully' }, 200
        return { 'message': 'Schedule not found' }, 404
    
    @staticmethod
    def delete_schedule(id_schedule: int):
        """
        This is the schedule controller that deletes a schedule.
        ---
        parameters:
        - id_schedule (int): The id of the schedule.
        responses:
        200:
            description: The schedule was successfully deleted.
        404:
            description: The schedule was not found.
        """
        schedule = Schedules.query.get(id_schedule)
        if schedule:
            db.session.delete(schedule)
            db.session.commit()
            return { 'message': 'Schedule deleted successfully' }, 200
        return { 'message': 'Schedule not found' }, 404
    
    # Assesment METHOD
    @staticmethod
    def get_available_appointment(day: str):
        schedules = Schedules.query.filter_by(day=day).all()
        if not schedules:
            return { 'message': 'Schedules not found' }, 404

        start_time = datetime.time(9, 0, 0)
        end_time = datetime.time(17, 0, 0)

        minimum_duration = datetime.timedelta(minutes=30)

        occupied_spaces = []
        for schedule in schedules:
            start = schedule.start_time
            end = add_to_time(start, datetime.timedelta(minutes=schedule.duration))
            occupied_spaces.append((start, end))
        
        available_appointments = []
        available_spaces = 0

        current_time = start_time
        while current_time < end_time:
            current_end_time = add_to_time(current_time, minimum_duration)

            if current_end_time > end_time:
                break
            
            if not any(start < current_end_time and end > current_time for start, end in occupied_spaces):
                available_appointments.append(current_time.strftime('%H:%M:%S'))
                available_spaces += 1
            current_time = current_end_time
        
        return {  'available_appointments': available_appointments, 'available_spaces': available_spaces }, 200