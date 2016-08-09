#!/usr/local/bin/python3
import requests
import json
import argparse
from pprint import pprint

# parser = argparse.ArgumentParser()
# parser.add_argument("command")
# args = parser.parse_args()

rpcUser = 'coinawesomerpc'
rpcPassword = 'Ap3HtegJ8SG46MuJoWDgZSMG1kbgnpo6C6sFzZoZWGpR'


def send(input_dict, verbose=True):
    if verbose:
        print("==============SENDING===============\n", input_dict)
    payload = json.dumps(input_dict)
    headers = {'content-type': 'application/json'}
    response = requests.get('http://localhost:8332', auth=(rpcUser, rpcPassword), headers=headers, data=payload)
    if verbose:
        print("==============RECEIVED==============")
        pprint(response.json())
    return response.json()

rawtxs = {
    "50_1": {
        "method": "createrawtransaction",
        "params": [
            [{"txid": "374437399348dd79dbf40860af9b3a94a1060b96322f56d39433cbceaff03108", "vout": 0}],
            {"AGewpgTEiUPxFyx7yFUNmGWdWdpawaTonS": 1}
        ]
    },
    "txid_0": {
        "method": "createrawtransaction",
        "params": [
            [{"txid": "0000000000000000000000000000000000000000000000000000000000000000", "vout": 65535}],
            {"AGewpgTEiUPxFyx7yFUNmGWdWdpawaTonS": 1}
        ]
    },
    "txid_f": {
        "method": "createrawtransaction",
        "params": [
            [{"txid": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "vout": 65535}],
            {"n4qD9AaB6TBdpZF915qh41oCTRSWhmasWV": 1000}
        ]
    }

}
response = send(rawtxs["txid_f"])
send({"method": "sendrawtransaction", "params": [response['result']]})
# ostensibly successful tx: 213d18dbf9c16ed57af2ab2a2adbecd4662fa62e8fc5b33fb1a4c9f2bea1c7fd
