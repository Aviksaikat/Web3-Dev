#!/usr/bin/python3
from avikChain import Blockchain, Block
import unittest

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_create_genesis_block(self):
        genesis_block = self.blockchain.create_genesis_block()
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.transactions, "Genesis block")
        self.assertEqual(genesis_block.previous_block, "0")

    def test_get_last_block(self):
        last_block = self.blockchain.get_last_block()
        self.assertEqual(last_block.index, 0)
        self.assertEqual(last_block.transactions, "Genesis block")
        self.assertEqual(last_block.previous_block, "0")

    def test_add_block(self):
        last_block = self.blockchain.get_last_block()
        new_block = Block(last_block.index + 1, "Transaction data", last_block.hash)
        self.blockchain.add_block(new_block)
        self.assertEqual(self.blockchain.get_last_block().index, 1)

    def test_is_chain_valid(self):
        self.assertFalse(self.blockchain.is_chain_valid())

        # modify a block and check if the chain is still valid
        last_block = self.blockchain.get_last_block()
        new_block = Block(last_block.index + 1, "Transaction data", last_block.hash)
        self.blockchain.add_block(new_block)
        self.blockchain.chain[1].data = "New transaction data"
        self.assertFalse(self.blockchain.is_chain_valid())

if __name__ == '__main__':
    unittest.main()
