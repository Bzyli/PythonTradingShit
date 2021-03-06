import flask
from flask import request, jsonify, send_from_directory, make_response, abort, send_file, url_for
from werkzeug.utils import redirect

app = flask.Flask(__name__)

startfile = open("start.html", "r")
start = startfile.read()


@app.route("/")
def yes():
    return redirect('./start')


@app.route("/start")
def begin():
    return start


@app.route("/dashboard", methods=["POST"])
def value_getter():

    return request.form


if __name__ == '__main__':
    app.run(debug=True)
