from flask import Flask, request
from flask_cors import CORS

from conn_web3.authentification_web3 import *
from conn_web3.connexion_web3 import *
from conn_web3.contract_soumission import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return str(count_offres())

@app.route('/offre/all')
def get_offre_all():
    return all_offres()
@app.route('/soumissions/all')
def get_all_soumission():
    return all_soumissions()
@app.route('/offre/descr')
def get_descr_offre():
    return get_desc_offre(2)

@app.route('/offre/detaille/<int:num>', methods=['GET'])
def get_detaille_offre(num):
    return get_dettaille(num)

@app.route('/offre/soumission/<int:num>', methods=['POST'])
def save_candidat(num):
    data = request.json
    result = save_candidature(num, data['societe'], data['telephone'], data['solution'], data['reference'])
    print(result)
    return result

@app.route('/offre', methods=['POST'])
def creer_offre():

    data = request.json
    result = save_offre(data['titre'], data['descritpion'], data['societe'], data['date_pub'], data['date_clos'])
    print(data)

    return result
@app.route('/evaluation')
def evaluer_offre():
    return evaluer()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    result = registrer_user(username, password)
    return result

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    password = data['password']
    username = data['username']
    is_authenticated = login(username,password)
    print(is_authenticated)
    return is_authenticated


@app.route('/offre/count')
def get_offre_count():
    return count_offres()

@app.route('/soumission/count')
def get_soumissioncount():
    return count_candidat()

@app.route('/soumisparoffre')
def soumis_par_offre():
    return nombr_cand_par_offre()

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)