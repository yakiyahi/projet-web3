from flask import Flask, request
from flask_cors import CORS
from src.web3.connexion_web3 import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return str(count_offres())

@app.route('/offre/all')
def get_offre_all():
    return all_offres()

@app.route('/offre/descr')
def get_descr_offre():
    return get_desc_offre(2)

@app.route('/offre/detaille/<int:num>', methods=['GET'])
def get_detaille_offre(num):
    return get_dettaille(num)



@app.route('/offre', methods=['POST'])
def creer_offre():

    data = request.json
    result = save_offre(data['titre'], data['descritpion'], data['societe'], data['date_pub'], data['date_clos'])
    print(data)

    return result


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)