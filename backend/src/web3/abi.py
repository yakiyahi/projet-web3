import json

def get_abi(file):
    abi = ""
    with open(file, "r") as fichier:
        donnees = json.load(fichier)
        abi = donnees["abi"]
    return abi