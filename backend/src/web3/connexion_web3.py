import json

from src.contances.contances import address_contract
from src.web3.abi import get_abi
from contances.contances import *


contract = web3.eth.contract(address=address_contract, abi=get_abi(fichier_json))


#creation fonction qui creer l'offre
def save_offre(title, description, societe, date_pub, date_clos):
    try:
        transaction = contract.functions.creerOffre(title, description,societe, date_pub, date_clos).transact(
            {
                "from": compte_address
            }
        )
        return "CREATE_SUCCESS"

    except Exception as e:
        return e

def all_offres():

    offres = contract.functions.getAllOffres().call()

    offre_json = []
    for offre in offres:
        offre_dict = {
            "numero": offre[0],
            "titre": offre[1],
            "description": offre[2],
            "societe": offre[3],
            "date_publication": offre[4],
            "date_cloture": offre[5]
        }
        offre_json.append(offre_dict)

    return json.dumps(offre_json)

def count_offres():

    offre_count = contract.functions.getOffreCount().call()

    return offre_count

#foncion qui recupere la description de l'offre
def get_desc_offre(numero):

    description = contract.functions.getDescriptionOffre(numero).call()

    return description

def get_dettaille(numero):

    offre = contract.functions.getOffre(numero).call()

    return json.dumps(offre)