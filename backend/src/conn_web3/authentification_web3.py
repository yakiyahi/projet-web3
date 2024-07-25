import json

from flask import jsonify

from contances.contances import auth_address
from conn_web3.abi import get_abi_auth
from contances.contances import *

contract = web3.eth.contract(address=auth_address, abi=get_abi_auth())
def registrer_user(user_name, password):
    try:
        tx_hash = contract.functions.register(user_name, password).transact({'from': compte_address})
        return jsonify({"message": "User registered successfully"})

    except Exception as e:
        print(e)
        return jsonify({"message": "User Not registered"})


def login(username,password):

    try:
        is_auth = contract.functions.authenticate(username,password).call({'from': compte_address})
        print(is_auth)
        return jsonify({"authenticated": is_auth})
    except:
        is_auth = 0
        return  jsonify({"authenticated": is_auth}) 