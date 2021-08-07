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

    def hash(self, block) :
        #dumps takes obj and makes it string
        encoded_block = json.dumps(block, sort_keys = True).encode()   
        return hashlib.sha256(encoded_block).hexdigest()          

    def is_chain_valid(self, chain) :
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain) :
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block) :
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] !='0000' :
                return False
            previous_block = block 
            block_index +=1
        return True    
            

#mining this blockchain

#creating a web app
app = Flask(__name__)

#creating a Blockchain
blockchain = Blockchain()

#mining a new block
@app.route('/mine_block', methods=['GET'])
def mine_block() :
    previous_block = blockchain.get_previous_block
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Block mined! It will be added to the chain.',
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash']}
    return jsonify(response), 200        




