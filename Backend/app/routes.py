from flask import Blueprint, Request, jsonify

auth = Blueprint('auth', __name__)

@auth.route("/input-konsumen", methods=['GET', 'POST'])
def input_konsumen():
  data = request.get_json()
  name = data.get('name')
  jenis = data.get('jenis')
  alamat = data.get('alamat')
  wa = data.get('wa')