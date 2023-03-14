#!/usr/bin/python3
import hashlib
import json
from datetime import datetime

class Block:
	"""
	a should have 
		- some data i.e. transation
		- previous hash
		- nonce

	kind of linked lists but don't have the link to the next block
	"""
	def __init__(self, index, transactions, previous_block, nonce=0):
		self.index = index
		self.timestamp = datetime.now()
		self.previous_block = previous_block
		self.transactions = transactions
		self.nonce = nonce

		self.hash = self.calulate_hash()

	"""
	https://stackoverflow.com/questions/2774361/json-output-sorting-in-python
	
	You are storing your values into a Python dict which has no inherent notion of ordering at all, it's just a key-to-value map. So your items lose all ordering when you place them into the values variable.
	In fact the only way to get a deterministic ordering would be to use `sort_keys=True`, which I assume places them in alphanumeric ordering
	"""
	def calulate_hash(self):
		data = json.dumps({
			"index": self.index,
			"timestamp": str(self.timestamp),
			"transaction": self.transactions,
			"previous_block": self.previous_block,
			"nonce": self.nonce,
		}, sort_keys=True).encode()

		#* get the value in hexadecimal
		return hashlib.sha256(data).hexdigest()

	# proof-of-work
	def mine_block(self, difficulty):
		#* check if the new hash the same number of trailing 0s as the difficulty
		while(self.hash[:difficulty] != '0' * difficulty):
			self.nonce += 1
			self.hash = self.calulate_hash()
		
		print(f"\nBlock mined: {self.hash}")
		return self.hash