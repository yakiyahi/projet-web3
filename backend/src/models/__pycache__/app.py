from flask import Flask, request, jsonify
from flask_cors import CORS
from connexion_web3 import *
import datetime


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


@app.route('/offre', methods=['POST'])
def creer_offre():
    data = request.json

    """ date_pub = datetime.datetime(2024, 5, 1)
    date_pub_final = int(date_pub.timestamp())
    date_clos = datetime.datetime(2024, 10, 1)
    date_clos_final = int(date_pub.timestamp()) """

    result = save_offre(data['titre'], data['descritpion'], data['date_pub'], data['date_clos'])
    print(data)

    return result


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)