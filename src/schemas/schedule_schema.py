from marshmallow import Schema, fields

class ScheduleSchema(Schema):
    day = fields.String(required=True)
    id_service = fields.Integer(required=True)
    start_time = fields.String(required=True)
    duration = fields.Integer(required=True)