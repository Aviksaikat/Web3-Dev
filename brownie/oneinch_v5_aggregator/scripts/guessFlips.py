#!/usr/bin/python3
from brownie import interface, multicall
from scripts.generate_path import *
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET




def main():
	tokens = ["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "0x6B175474E89094C44Da98b954EedeAC495271d0F"]

	possible_paths = generate_all_paths(tokens)
	path_for_1inch = generate_path_for_1inch(possible_paths)

	oneInch_aggregator = interface.I1inchAggregator("0x07D91f5fb9Bf7798734C3f606dB065549F6893bb")
	uniswapV2 = interface.ISwapV2Router02("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

	#print(dir(oneInch_aggregator))

	data = []
	amount = 1 * 10 ** 18 # output token decimal i.e. DAI

	multicall(address="0xcA11bde05977b3631167028862bE2a173976CA11")
	#multicall(address="0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696")
	# with multicall:
	# 	for path in possible_paths:
	# 		#result = oneInch_aggregator.getRate(tokens[0], tokens[1], True)
	# 		result = uniswapV2.getAmountsOut(amount, path)
	# 		data.append(result)
	# print(data)

	rate = oneInch_aggregator.getRate(tokens[0], tokens[1], True)
	print(rate)

	
