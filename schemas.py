from marshmallow import Schema, fields, validate

from common.states import STATES


class PersonalDataSchema(Schema):
    full_name = fields.Str(required=True)
    national_id = fields.Str(required=True)
    position = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True, validate=validate.OneOf(STATES))
    is_correct = fields.Bool(required=True)
    titularity = fields.Str(required=True, validate=validate.OneOf(["titular", "dependant"]))
    phone = fields.Str(required=True)
    email = fields.Email(required=True)
    birth_date = fields.Date(format="%Y-%m-%d")
    gender = fields.Str(required=True, validate=validate.OneOf(["male", "female"]))
    weight = fields.Int(required=True)
    height = fields.Int(required=True)
    min_pressure = fields.Str()
    max_pressure = fields.Str()
    know_pressure = fields.Bool(required=True)


class DiseasesSchema(Schema):
    diseases = fields.List(fields.Dict(), many=True)
    remarks = fields.Str()


class DietSchema(Schema):
    type = fields.Str(required=True, validate=validate.OneOf(["Vegetariano", "Vegano", "Sem Restrição"]))
    options = fields.List(fields.Str)


class FormSchema(Schema):
    page_1 = fields.Nested(PersonalDataSchema(), required=True)
    page_2 = fields.Nested(DiseasesSchema(), required=True)
    page_3 = fields.Nested(DietSchema(), required=True)
