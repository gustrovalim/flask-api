from flask import Flask
from api.acucar_e_alcool import acucar_e_alcool_route

app = Flask(__name__)
app.register_blueprint(acucar_e_alcool_route)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")