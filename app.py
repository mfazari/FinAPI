from flask import Flask, render_template, make_response
from flask_cors import CORS


# import routes (v indicating version)
from routes.test.test_route import test_route
from routes.manager.v1.manager import manager_page
from routes.error_handling.errors import error

app = Flask(__name__)
CORS(app)
app.register_blueprint(test_route)
app.register_blueprint(manager_page)
app.register_blueprint(error)


@app.route("/")
def index():
    return render_template("index.html", title='Home')


if __name__ == "__main__":
    app.run()
