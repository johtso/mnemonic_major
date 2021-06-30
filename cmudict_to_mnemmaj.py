from collections import defaultdict
from operator import itemgetter
from nltk.corpus import cmudict

OUT_FILE_NAME = 'mnemmaj_dict.txt'

phenome_translation = {
    'B': '9',
    'CH': '6',
    'D': '1',
    'DH': '1',
    'TH': '1',
    'ER': '4',
    'F': '8',
    'G': '7',
    'JH': '6',
    'K': '7',
    'L': '5',
    'M': '3',
    'N': '2',
    'NG': '27',
    'P': '9',
    'R': '4',
    'S': '0',
    'SH': '6',
    'T': '1',
    'V': '8',
    'Z': '0',
    'ZH': '6',
}

def convert_entry(entry):
    word, phenomes = entry
    enc = ''
    for phenome in phenomes:
        phenome = phenome.strip('012')
        enc += phenome_translation.get(phenome, '')
    return word, enc

mnemmaj_dict = defaultdict(set)

for entry in cmudict.entries():
    word, enc = convert_entry(entry)
    if enc:
        mnemmaj_dict[enc].add(word)

with open(OUT_FILE_NAME, 'w') as outfile:
    for enc, words in iter(sorted(mnemmaj_dict.items(), key=lambda x: (len(x[0]), x[0]))):
        outfile.write('%s;%s\n' % (enc, ','.join(sorted(words))))