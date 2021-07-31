import datetime
import hashlib
import json
from flask import Flask, jsonify
from flask.json import htmlsafe_dumps

#building the blockchain
class Blockchain :
    def __init__(self) :
        self.chain = []
        #genesis block
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash) :
        block = {'index' : len(self.chain)+1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' :  proof,
                 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block 

    def get_previous_block(self) : 
        #last index can be accessed by using -1 as index.
        return self.chain[-1]                   

    def proof_of_work(self, previous_proof) :
        new_proof = 1
        check_proof = False
        while check_proof is False :
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            #range from 0 to 3 index for checking four leading zeros of finding new proof.
            if hash_operation[:4] == '0000' :
                check_proof = True
            else :
                new_proof+=1
        return new_proof            






#mining this blockchain