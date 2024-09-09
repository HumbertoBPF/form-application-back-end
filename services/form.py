from flask import request
from marshmallow import ValidationError

from schemas import FormSchema
from utils.cors import MethodViewWithCors, cors


class FormView(MethodViewWithCors):
    @cors
    def post(self):
        data = request.json

        try:
            data = FormSchema().load(data)
        except ValidationError as e:
            return e.messages, 400

        print(data)
        return "", 200
