#!/usr/bin/python3
#? theory https://www.youtube.com/watch?v=zVqczFZr124
from block import Block

class Blockchain():
    def __init__(self):
        #* mine the genesis block
        self.chain = [self.create_genesis_block()]
        #* for Proof-of-work
        self.difficulty = 4

    def create_genesis_block(self):
        # index, transactions, previous_block, nonce=0
        return Block(0, "Genesis block", "0")

    def get_last_block(self):
        #* return the latest block
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        #* using POW to mine the block
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            if(current_block.hash != current_block.calulate_hash()):
                return False
            if(current_block.previous_block != prev_block.hash):
                return False
        return True


