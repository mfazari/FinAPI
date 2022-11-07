from flask import render_template, Blueprint

test_route = Blueprint("test_route", __name__, template_folder="templates")


@test_route.route("/test", methods=["GET"])
def test():
    return render_template("test.html", title="Test")
