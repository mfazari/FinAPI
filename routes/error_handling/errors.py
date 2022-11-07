from flask import Flask, render_template, make_response, Blueprint


error = Blueprint("error_handlers", __name__, template_folder="templates")


@error.app_errorhandler(404)
def not_found(error):
    return make_response(render_template("404.html"), 404)


@error.app_errorhandler(400)
def bad_request(error):
    return make_response(render_template("400.html"), 400)


@error.app_errorhandler(500)
def server_error(error):
    return make_response(render_template("500.html"), 500)
