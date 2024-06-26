import json
from src.contances.contances import *
from src.web3.abi import *
from src.models.recupere_info import *

contract = web3.eth.contract(address=soumission_address, abi=get_abi_submit())

#Candidater a une soumission
def save_candidature(numero_contrat, candidat, solution, reference):
    try:
        ref_cli = str(recupere_societe(reference))
        print("societe ", ref_cli)
        cout = str(recupere_prix(solution))
        delais = str(recupere_duree(solution))

        transaction = contract.functions.ajouterSoumission(soumission_address, numero_contrat, candidat, cout, delais, ref_cli).transact(
            {
                "from": compte_address
            }
        )
        return "CREATE_SUCCESS"

    except Exception as e:
        return e

def all_soumissions():

    soumissions = contract.functions.listeToutesSoumissions().call()

    soumis_json = []
    for soumission in soumissions:
        print(soumission)
        soumis_dict = {
            "numero": soumission[0],
            "soumissionaire": soumission[1],
            "numeroContrat": soumission[2],
            "societe": soumission[3],
            "prix": soumission[4],
            "duree": soumission[5],
            "references": soumission[6],
            "decision": "ENCOURS"
        }

        soumis_json.append(soumis_dict)


    return json.dumps(soumis_json)

def evaluer():
    prix = 0
    submitions =  contract.functions.listeToutesSoumissions().call()
    for submit in submitions:
        prix = recupere_prix("prix"+str(submit[4]))
        print(prix)
    return ""