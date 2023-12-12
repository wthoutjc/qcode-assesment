from marshmallow import Schema, fields

class ServiceSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=False)