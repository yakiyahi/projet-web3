from flask import Flask, request
from flask_cors import CORS
from src.web3.connexion_web3 import *
from src.web3.contract_soumission import *

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
    return  all_soumissions()
@app.route('/offre/descr')
def get_descr_offre():
    return get_desc_offre(2)

@app.route('/offre/detaille/<int:num>', methods=['GET'])
def get_detaille_offre(num):
    return get_dettaille(num)

@app.route('/offre/soumission/<int:num>', methods=['POST'])
def save_candidat(num):
    data = request.json
    result = save_candidature(num, data['societe'], data['solution'], data['reference'])
    print(result)
    return result

@app.route('/offre', methods=['POST'])
def creer_offre():

    data = request.json
    result = save_offre(data['titre'], data['descritpion'], data['societe'], data['date_pub'], data['date_clos'])
    print(data)

    return result
@app.route('/soumissions/evaluer')
def evaluer_offre():
    return evaluer()

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)