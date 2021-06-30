import sys
import os

from nltk.corpus import wordnet as wn

from mnemmaj import tree_of_splits, explore, parse_digit_to_word_list


dummy, width = os.popen('stty size', 'r').read().split()

lookup_table = parse_digit_to_word_list()

seq = sys.argv[1]

# max_parts = int(sys.argv[2])

print('seq:', seq)
# print 'max_parts:', max_parts

# tree = tree_of_splits(seq, 1)

# def node_test(node):
#     return (node in lookup_table)

def iterchunks(iterator, n):
    """Iterate returning n results at a time"""
    iterator = iter(iterator)
    return zip(*([iterator]*n))

# chunks = list(explore(tree, node_test=node_test))[0]
# print chunks
# words = [lookup_table[chunk] for chunk in chunks]

words = lookup_table[seq]

words = [word for word in words if any((ss.pos == 'n' for ss in wn.synsets(word)))]

max_word_length = max([len(word) for word in words]) + 3

cols = (int(width) / max_word_length) - 1

for line in iterchunks(words, cols):
    for word in line:
        print(word.ljust(max_word_length))
    print("...")