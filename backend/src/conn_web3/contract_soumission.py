import json
from contances.contances import *
from conn_web3.abi import *
from models.recupere_info import *
from models.evaluer_candidature import evaluer_candidats
from postgres_con.connextion_db import *


contract = web3.eth.contract(address=soumission_address, abi=get_abi_submit())

#Candidater a une soumission
def save_candidature(numero_contrat, candidat,telephone, solution, reference):
    try:
        ref_cli = str(reference)
        print("societe ", ref_cli)
        cout = str(recupere_prix(solution))
        delais = str(recupere_duree(solution))

        transaction = contract.functions.ajouterSoumission(soumission_address, numero_contrat, candidat, telephone, cout, delais, ref_cli).transact(
            {
                "from": compte_address
            }
        )
        return "CREATE_SUCCESS"

    except Exception as e:
        return e


def soumissions():
    soumissions = contract.functions.listeToutesSoumissions().call()

    soumis_json = []
    for soumission in soumissions:
        soumis_dict = {
            "numero": soumission[0],
            "soumissionaire": soumission[1],
            "numeroContrat": soumission[2],
            "societe": soumission[3],
            "telephone": soumission[4],
            "prix": soumission[5],
            "duree": soumission[6],
            "references": soumission[7]
        }
        soumis_json.append(soumis_dict)

    return soumis_json

def all_soumissions():

    soumis_json = soumissions()
    return json.dumps(soumis_json)

def grouper(candidatures):
    cnds = []
    meilleurs = []
    grouped_candidatures = {}
    for candidature in candidatures:
        num_appel_offre = candidature['numeroContrat']
        if num_appel_offre not in grouped_candidatures:
            grouped_candidatures[num_appel_offre] = []
        grouped_candidatures[num_appel_offre].append(candidature)

    for num_appel_offre, candidatures_list in grouped_candidatures.items():
        #print(f"Appel d'offre {num_appel_offre}:")
        #print(f"  - {candidatures_list}")
        decision, meilleur = evaluer_candidats(candidatures_list)
        cnds.append(decision)
        meilleurs.append(meilleur)
    return cnds, meilleurs

def calc_moy_passe(nom):
    moy = 0
    notes = get_enterprise_info(nom)
    for note in notes:
        moy = sum(note)/len(note)
        return moy

def evaluer():
    clients = []
    submitions = soumissions()
    print(submitions)
    for cli in submitions:
        cli["references"] = len(cli["references"].split(",")) if cli['references'] != "" else 0
        cli["prix"] = int(cli["prix"].replace(" ", ""))
        cli["duree"] = int(re.findall(r'\d+', cli["duree"])[0])
        cli['passe'] = calc_moy_passe(cli['societe'])
        clients.append(cli)


    decision, meilleur = grouper(clients)
    #decision.append(meilleur)
    #print("meilleur: ", decision[-1])
    return json.dumps(decision)

def count_candidat():

    candidat_count = contract.functions.nombreSoumissions().call()

    return str(candidat_count)     