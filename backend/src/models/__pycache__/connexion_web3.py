from web3 import Web3, HTTPProvider
import json
from abi import get_abi


address_contract = "0xc1c8a82E2e0D70534e3A329e50e4c2bf8a8753Bf"
nonce = ""
compte_address = "0x4dc6A82F54b2e50AB156377970075E8dd5FD2B5d"
nonce = ""
web3 = Web3(HTTPProvider('http://localhost:7545'))
gas_price =""
contract = web3.eth.contract(address=address_contract, abi=get_abi())


#creation fonction qui creer l'offre
def save_offre(title, description, date_pub, date_clos):
    try:
        transaction = contract.functions.creerOffre(title, description, date_pub, date_clos).transact(
            {
                "from": compte_address
            }
        )
        return "CREATE_SUCCESS"

    except Exception as e:
        return e

def all_offres():

    count = contract.functions.getOffreCount().call()
    offres = contract.functions.getAllOffres().call()

    offre_json = []
    for offre in offres:
        offre_dict = {
            "numero": offre[0],
            "titre": offre[1],
            "description": offre[2],
            "date_publication": offre[3],
            "date_cloture": offre[4]
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