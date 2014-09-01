from flask import make_response

TEMPLATE_DIR = "talisman/templates/"


def static_response(path):
    return make_response(open(TEMPLATE_DIR+path).read())
