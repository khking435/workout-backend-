from marshmallow import Schema, fields, validate

class UserWorkoutSchema(Schema):
    userworkout_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    workout_id = fields.Int(required=True)
    startdate = fields.Date(required=True)
    completiondate = fields.Date(required=True)
    feedback = fields.Str(validate=validate.Length(min=1))
