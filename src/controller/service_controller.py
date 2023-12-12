# Model
from src.models.models import Services, db
from sqlalchemy.exc import IntegrityError

class ServiceController:
    @staticmethod
    def create_service(data: dict):
        """
        This is the service controller that creates a service.
        ---
        parameters:
        - data (dict): The data of the service.
        responses:
        200:
            description: The service was successfully created.
        400:
            description: The service was not successfully created.
        """
        new_service = Services(name=data['name'], description=data['description'])
        db.session.add(new_service)
        try:
            db.session.commit()
            return { 'message': 'Service created successfully' }, 200
        except IntegrityError:
            db.session.rollback()
            return { 'message': 'Service already exists' }, 400
    
    @staticmethod
    def get_services():
        """
        This is the service controller that gets all services.
        ---
        parameters:
        - None
        responses:
        200:
            description: The services were successfully retrieved.
        400:
            description: The services were not successfully retrieved.
        """
        services = Services.query.all()
        return { 'services': [service.serialize() for service in services] }, 200
    
    @staticmethod
    def get_service_by_id(id_service: int):
        """
        This is the service controller that gets a service by id.
        ---
        parameters:
        - id_service (int): The id of the service.
        responses:
        200:
            description: The service was successfully retrieved.
        404:
            description: The service was not found.
        """
        service = Services.query.get(id_service)
        if service:
            return { 'service': service.serialize() }, 200
        return { 'message': 'Service not found' }, 404
    
    @staticmethod
    def update_service(id_service: int, data: dict):
        """
        This is the service controller that updates a service.
        ---
        parameters:
        - id_service (int): The id of the service.
        - data (dict): The data of the service.
        responses:
        200:
            description: The service was successfully updated.
        404:
            description: The service was not found.
        """
        service = Services.query.get(id_service)
        if service:
            service.name = data['name']
            service.description = data['description']
            db.session.commit()
            return { 'message': 'Service updated successfully' }, 200
        return { 'message': 'Service not found' }, 404
    
    @staticmethod
    def delete_service(id_service: int):
        """
        This is the service controller that deletes a service.
        ---
        parameters:
        - id_service (int): The id of the service.
        responses:
        200:
            description: The service was successfully deleted.
        404:
            description: The service was not found.
        """
        service = Services.query.get(id_service)
        if service:
            db.session.delete(service)
            db.session.commit()
            return { 'message': 'Service deleted successfully' }, 200
        return { 'message': 'Service not found' }, 404