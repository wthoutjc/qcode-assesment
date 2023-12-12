from flask import Blueprint, request, jsonify, make_response

#  Service
from src.controller.schedule_controller import ScheduleController

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/schedules', defaults={"id": None})
@schedule_bp.route('/schedules/<int:id>')
def schedule_route(id:int):
    """
    This is the schedule route that gets all schedules, gets a schedule by id, creates a schedule, updates a schedule and deletes a schedule.
    ---
    parameters:
    - id (int): The id of the schedule.
    - day (int): The day of the schedule.
    - start_time (time): The start time of the schedule.
    - duration (int): The duration of the schedule.
    responses:
    200:
        description: The schedules were successfully retrieved.
    400:
        description: The schedules were not successfully retrieved.
    404:
        description: The schedule was not found.
    """
    if id:
        response, status = ScheduleController.get_schedule_by_id(id)
    else:
        response, status = ScheduleController.get_schedules()
    return make_response(jsonify(response), status)


@schedule_bp.route('/schedules/<string:day>', methods=['GET'])
def schedule_by_day_route(day:str):
    """
    This is the schedule route that gets a schedule by day.
    ---
    parameters:
    - day (string): The day of the schedule.
    responses:
    200:
        description: The schedule was successfully retrieved.
    404:
        description: The schedule was not found.
    """
    if request.method == "GET":
        response, status = ScheduleController.get_schedule_by_day(day)
        return make_response(jsonify(response), status)
    return make_response(jsonify({'message': 'Schedule not found'}), 404)

@schedule_bp.route('/available-appointment/<string:day>', methods=['GET'])
def available_appointment_route(day:str):
    """
    This is the available appointment route that gets all available appointments.
    ---
    parameters:
    - day (str): The day of the schedule.
    responses:
    200:
        description: The available appointments were successfully retrieved.
    400:
        description: The available appointments were not successfully retrieved.
    404:
        description: The schedule was not found.
    """
    if request.method == "GET":
        response, status = ScheduleController.get_available_appointment(day)
        return make_response(jsonify(response), status)
    return make_response(jsonify({'message': 'Schedule not found'}), 404)