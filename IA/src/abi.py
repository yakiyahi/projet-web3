import json

fichier_json = "src/contracts/AppelOffres.json"

def get_abi():
    abi = ""
    with open(fichier_json, "r") as fichier:
        donnees = json.load(fichier)
        abi = donnees["abi"]
    return abi