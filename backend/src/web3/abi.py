import json

fichier_json = "./contracts/AppelOffres.json"
soumission_file_json = "./contracts/ContratSoumissions.json"

def get_abi():
    abi = ""
    with open(fichier_json, "r") as fichier:
        donnees = json.load(fichier)
        abi = donnees["abi"]
    return abi

def get_abi_submit():
    abi = ""
    with open(soumission_file_json, "r") as fichier:
        donnees = json.load(fichier)
        abi = donnees["abi"]
    return abi