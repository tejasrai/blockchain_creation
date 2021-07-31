import datetime
import hashlib
import json
from flask import Flask, jsonify

#building the blockchain
class Blockchain :
    def __init__(self) :
        self.chain = []
        #genesis block
        self.create_block(proof = 1, previous_hash = '0')

    



#mining this blockchain