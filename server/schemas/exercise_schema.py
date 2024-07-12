from marshmallow import Schema, fields, validate

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    sets = fields.Int(required=True)
    reps = fields.Int(required=True)
    weight = fields.Int(required=True)
