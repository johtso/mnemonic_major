from __future__ import with_statement
from collections import defaultdict
from itertools import combinations

from utils import multi_split

def valid_cut_combos(length, max_parts=None, min_part_len=1):
    """Find all possible ways in which a sequence could be split and return the
    indices of the split points.

    """
    if not max_parts:
        max_parts = length / min_part_len
    valid_split_points = range(1, length)

    for parts in range(1, max_parts + 1):
        cuts = parts - 1
        for cut_combo in combinations(valid_split_points, cuts):
            yield cut_combo

def all_splits(seq, max_parts=None, min_part_len=1):
    """Iterate over the sequence split in every possible way"""
    for split_points in valid_cut_combos(len(seq), max_parts):
        yield multi_split(seq, split_points)

def explore(node, path=[], node_test=None):
    if node == {}:
        yield path
    else:
        sorted_keys = sorted(node.keys(), key=len, reverse=True)
        for node_key in sorted_keys:
            if node_test and not node_test(node_key):
                continue

            child_node = node[node_key]
            for result in explore(child_node, path+[node_key], node_test):
                yield result

def tree_of_splits(seq, max_parts):
    tree = {}
    for split_seq in all_splits(seq, max_parts):
        current_node = tree
        for chunk in split_seq:
            new_node = {}
            if chunk not in current_node:
                current_node[chunk] = new_node
                current_node = new_node
            else:
                current_node = current_node[chunk]
    return tree

def parse_digit_to_word_list():
    def parse_line(line):
        num, words = line.split(';', 1)
        return num, words.split(',')

    parsed = {}
    with open('mnemmaj_dict.txt', 'r') as fh:
        lines = (line.rstrip() for line in fh if line)
        lines = (line for line in lines if line)

        for line in lines:
            num, words = parse_line(line)
            parsed[num] = words
        
    return parsed