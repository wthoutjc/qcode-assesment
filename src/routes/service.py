from flask import Blueprint, request, jsonify, make_response

# Schema
from src.schemas.service_schema import ServiceSchema

#  Service
from src.controller.service_controller import ServiceController

service_bp = Blueprint('service', __name__)

@service_bp.route('/services', defaults={"id": None}, methods=['GET', 'POST'])
@service_bp.route('/services/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def service_route(id:int):
    """
    This is the service endpoint of the API.
    ---
    parameters:
    - id (int): The id of the service.
    responses:
    200:
        description: The service was successfully retrieved.
    400:
        description: The service was not successfully retrieved.
    404:
        description: The service was not found.
    """
    if request.method == "GET":
        if id:
            response, status = ServiceController.get_service_by_id(id)
        else:
            response, status = ServiceController.get_services()
        return make_response(jsonify(response), status)
    elif request.method == "POST":
        service_data = request.get_json()
        
        # Validate data
        errors = ServiceSchema().validate(service_data)
        if errors:
            return make_response(jsonify({'error': errors}), 400)
        
        response, status = ServiceController.create_service(service_data)
        return make_response(jsonify(response), status)
    elif request.method == "PUT":
        service_data = request.get_json()
        
        # Validate data
        errors = ServiceSchema().validate(service_data)
        if errors or not id:
            return make_response(jsonify({'error': errors}), 400)
        
        response, status = ServiceController.update_service(id, service_data)
        return make_response(jsonify(response), status)
    elif request.method == "DELETE":
        if id:
            response, status = ServiceController.delete_service(id)
            return make_response(jsonify(response), status)
        return make_response(jsonify({'message': 'Service not found'}), 404)