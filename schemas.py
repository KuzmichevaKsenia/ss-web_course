from marshmallow import Schema, fields


class EmployeeSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    position = fields.Str(required=True)


class EmployeeCreateOrUpdateSchema(Schema):
    name = fields.Str(required=True)
    position = fields.Str(required=True)
