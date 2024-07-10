from marshmallow import Schema, fields, validate

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    date = fields.Date(required=True)
    duration = fields.Int(required=True)
    type = fields.Str(required=True)
