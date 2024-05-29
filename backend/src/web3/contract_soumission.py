import json
from abi import get_abi
from src.contances.contances import *


contract = web3.eth.contract(address=soumission_address, abi=get_abi(soumission_file_json))

#Candidater a une soumission
def save_candidature(title, description, societe, date_pub, date_clos):
    try:
        transaction = contract.functions.creerOffre(title, description,societe, date_pub, date_clos).transact(
            {
                "from": compte_address
            }
        )
        return "CREATE_SUCCESS"

    except Exception as e:
        return e
