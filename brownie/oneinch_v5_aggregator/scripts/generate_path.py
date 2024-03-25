#!/usr/bin/python3
from itertools import combinations, permutations
from typing import List
from loguru import logger
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def has_consecutive_repeat(seq):
    return any(x == y for x, y in zip(seq, seq[1:]))


def generate_path_for_1inch(possible_paths: List[tuple]) -> set:
    pairs = []

    for element in possible_paths:
        for pair in combinations(element, 2):
            if pair[0] != pair[1] and pair not in pairs:
                pairs.append(pair)
    return pairs


def generate_all_paths(nodes: list) -> list[list]:
    paths = set()
    # Iterate over all nodes as starting nodes
    for start_node in nodes:
        # Generate combinations of different lengths starting from 1
        for r in range(len(nodes)):
            # Generate combinations without repetition
            for comb in combinations(nodes, r):
                # Generate all permutations of the combination
                perms = set(permutations(comb))
                # Generate paths with the start node and permutations
                for perm in perms:
                    path = tuple([start_node] + list(perm) + [start_node])
                    if not has_consecutive_repeat(path):
                        paths.add(path)
    print(f"{green}[*]Generated {red}{len(paths)} {green}Number Of Combinations{reset}")
    return list(paths)


def main():
    # start_node = "DAI" # no need after the new implementaion
    # nodes = ["A", "C", "D", "E"]
    nodes = ["WBTC", "WETH", "USDC"]
    print(generate_all_paths(nodes))


if __name__ == "__main__":
    main()
