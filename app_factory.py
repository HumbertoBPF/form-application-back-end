from flask import Flask

from services.food import FoodView
from services.form import FormView


def create_app():
    app = Flask(__name__)

    app.add_url_rule("/getAlimentacao", view_func=FoodView.as_view("get-alimentacao"))
    app.add_url_rule("/submitFormulario", view_func=FormView.as_view("submit-formulario"))

    return app
