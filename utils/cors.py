from flask import make_response
from flask.views import MethodView

from settings import ACCESS_CONTROL_ALLOW_METHODS, ACCESS_CONTROL_ALLOW_HEADERS, ACCESS_CONTROL_ALLOW_ORIGINS


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", ACCESS_CONTROL_ALLOW_ORIGINS)
    response.headers.add('Access-Control-Allow-Headers', ACCESS_CONTROL_ALLOW_HEADERS)
    response.headers.add('Access-Control-Allow-Methods', ACCESS_CONTROL_ALLOW_METHODS)
    return response


class MethodViewWithCors(MethodView):
    def options(self, *args, **kwargs):
        return _build_cors_preflight_response()


def cors(endpoint):
    def add_cors_headers(*args, **kwargs):
        value = *endpoint(*args, **kwargs), {
            "Access-Control-Allow-Origin": ACCESS_CONTROL_ALLOW_ORIGINS
        }
        return value

    return add_cors_headers
