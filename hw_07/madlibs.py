import random

sentence =  "There once was a man named <ProperNoun> and he loved to eat <noun> a lot. This man lived in <country> and spoke <language> . He had a <adjective> <animal> as a companion, and his most prized posession in his house was a <adjective> <furniture> . He grew old and <verb> until he layed down <adverb> and <verb> "
ProperNoun=['Irvington','Jerry', 'Elizabeth','Hillside']
noun=['greenbeans', 'cars','markers','cologne']
verb=['died', 'laughed', 'smoked', 'twerked']
adverb=['merrily','terribly','cryptically','bootyliciously']
adjective=['fat','childish','soggy','beautiful','muscular']
animal=['lion', 'zebra', 'lil piggy', 'hippo', 'house cat', 'fat fly']
furniture=['chair', 'bed','desk','mirror', 'strange painting']
country=['Israel','Cuba','Syria', 'Turkey','Uzbekistan','China']
language=['Spanish','Hebrew','Mandarin','Cantonese','Russian']

category  = ['<ProperNoun>','<noun>','<verb>','<adverb>','<adjective>','<animal>','<furniture>','<country>','<language>']
words = [ProperNoun,noun,verb,adverb,adjective,animal,furniture,country,language]

dictionary = {}

for i, j in zip(category, words):
    dictionary[i] = j


def MADLIB(s,d):
   
    product = []
    d['<language>'] = [random.choice(d['<language>'])]
    
    for i in s.split():
        if i in d:
            product.append(random.choice(d[i]))
        else:
            product.append(i)
    return ' '.join(product)

print(MADLIB(sentence, dictionary))
