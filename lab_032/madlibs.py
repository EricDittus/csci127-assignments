#Eric Dittus & Chana Abramov
import random
ProperNoun=['Irvington','Jerry', 'Elizabeth','Hillside']
noun=['greenbeans', 'cars','markers','cologne']
verb=['died', 'laughed', 'smoked', 'twerked']
adverb=['merrily','terribly','cryptically','bootyliciously']
adjective=['fat','childish','soggy','beautiful','muscular']
animal=['lion', 'zebra', 'lil piggy', 'hippo', 'house cat', 'fat fly']
furniture=['chair', 'bed','desk','mirror', 'a strange painting']
country=['Israel','Cuba','Syria', 'Turkey','Uzbekistan','China']
language=['Spanish','Hebrew','Mandarin','Cantonese','Russian']
Madlib= "There once was a man named <ProperNoun> and he loved to eat <noun> a lot. This man lived in <country> and spoke <language> . He had a <adjective> <animal> as a companion, and his most prized posession in his house was a <adjective> <furniture> . He grew old and <verb> until he layed down <adverb> and <verb> "

def MADLIB(Madlib):
    list_madlib = Madlib.split(' ')
    i=0
    space=" "
    while i< len(list_madlib)-1:
        if "<" in list_madlib[i]:
            if "ProperNoun" in list_madlib[i]:
                index = random.randint(0, len(ProperNoun)-1)
                list_madlib[i]=ProperNoun[index]
            if "noun" in list_madlib[i]:
                index = random.randint(0, len(noun)-1)
                list_madlib[i]=noun[index]
            if ("verb" in list_madlib[i]) and ("ad" not in list_madlib[i]):
                index = random.randint(0, len(verb)-1)
                list_madlib[i]=verb[index]
            if "adverb" in list_madlib[i]:
                index = random.randint(0,len(adverb)-1)
                list_madlib[i]=adverb[index]
            if "animal" in list_madlib[i]:
                index = random.randint(0,len(animal)-1)
                list_madlib[i]=animal[index]
            if "adjective" in list_madlib[i]:
                index = random.randint(0,len(adjective)-1)
                list_madlib[i]=adjective[index]
            if "furniture" in list_madlib[i]:
                index = random.randint(0,len(furniture)-1)
                list_madlib[i]=furniture[index]
            if "country" in list_madlib[i]:
                index = random.randint(0,len(country)-1)
                list_madlib[i]=country[index]
            if "language" in list_madlib[i]:
                index = random.randint(0,len(language)-1)
                list_madlib[i]=language[index]
 
        i+=1
    return space.join(list_madlib)

print(MADLIB(Madlib))
