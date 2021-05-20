from flask import Flask, render_template, request, json
from flask_basicauth import BasicAuth
from keras import backend as K
from model import predict

app = Flask(__name__)

app.config["BASIC_AUTH_USERNAME"] = "thomas"
app.config["BASIC_AUTH_PASSWORD"] = "Pynchon"
app.config["BASIC_AUTH_FORCE"] = True

basic_auth = BasicAuth(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def rest_predict():
    # Before prediction
    K.clear_session()
    image = str(
        request.form.get("image")
        if request.form.get("image") is not ""
        else request.args.get("image")
    )
    animal = predict(image)
    result = {"result": animal}
    response = app.response_class(
        response=json.dumps(result), status=200, mimetype="application/json"
    )
    # Before prediction
    K.clear_session()
    return response


app.run(host="0.0.0.0", port=5000, debug=True)
