

def addline(d,line):
    my_list = []
    line=line.lower()
    new_line = line.split()
    i=0
    while i <= len(new_line)-1:
        word = new_line[i]
        char=word[0]
        if char in d:
            my_list=d[char]
            my_list.append(word)
            d[char]=my_list
        else:
            my_list = [word]
            d[char]= my_list
        i += 1
    return d

print(addline({'a':['okay']},"apples octopus"))

def main():
    d={}
    addline(d,"apples and octopi love water")
    addline(d,"if i were a fish, I would Hate to Swim")
    addline(d,"How much Wood")
    addline(d,"could a Woodchuck chuck")
    addline(d,"if a Woodchuck could chuck wood")
    return d

print(main())

def spellcheck(d,word):
    word=word.lower()
    if word[0] in d:
        if word in d[word[0]]:
          return True
        else:
          return False

    else:
        return False

print(spellcheck(main(),'gotcha'))
print(spellcheck(main(),'apples'))
