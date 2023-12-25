from flask import Blueprint
import json


acucar_e_alcool_route = Blueprint('acucar_e_alcool', __name__)

@acucar_e_alcool_route.route("/api/modelo/acucar_e_alcool", methods=['POST'])
def acucar_e_alcool():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 