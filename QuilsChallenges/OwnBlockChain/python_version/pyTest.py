#!/usr/bin/python3
import sys
sys.path.append("/home/avik/Desktop/practice/web3/Development/QuilsChallenges/OwnBlockChain/python_version")
from avikChain import Blockchain, Block


def test_create_genesis_block():
    blockchain = Blockchain()
    genesis_block = blockchain.create_genesis_block()
    assert genesis_block.index == 0
    assert genesis_block.transactions == "Genesis block"
    assert genesis_block.previous_block == "0"
    print("test_create_genesis_block passed")

def test_get_last_block():
    blockchain = Blockchain()
    last_block = blockchain.get_last_block()
    assert last_block.index == 0
    assert last_block.transactions == "Genesis block"
    assert last_block.previous_block == "0"
    print("test_get_last_block passed")

def test_add_block():
    blockchain = Blockchain()
    last_block = blockchain.get_last_block()
    new_block = Block(last_block.index + 1, "Transaction data", last_block.hash)
    blockchain.add_block(new_block)
    assert blockchain.get_last_block().index == 1
    print("test_add_block passed")

def test_is_chain_valid():
    blockchain = Blockchain()
    assert not blockchain.is_chain_valid()

    # modify a block and check if the chain is still valid
    last_block = blockchain.get_last_block()
    new_block = Block(last_block.index + 1, "Transaction data", last_block.hash)
    blockchain.add_block(new_block)
    blockchain.chain[1].data = "New transaction data"
    assert not blockchain.is_chain_valid()
    print("test_is_chain_valid passed")


if __name__ == '__main__':
    test_create_genesis_block()
    test_get_last_block()
    test_add_block()
    test_is_chain_valid()
    print("All tests passed!")
