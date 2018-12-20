def canMakeWord(letters,word):
    count = 0
    i=0
    while i <= len(word) -1:
        if word[i] in letters:
            count += 1
            letters[letters.find(word[i])]==''
        i +=1
    if count == len(word):
        return True
    else:
        return False

print(canMakeWord("ladilmy","daily"))

def withWild(letters,word):
    count = 0
    i=0
    while i <= len(word)-1:
        if word[i] in letters:
            count += 1
            letters[letters.find(word[i])]==''

        if (word[i] not in letters) and ('?' in letters):
                count += 1
                letters[letters.find('?')]==''
        i+=1

    if count == len(word):
        return True
    else:
        return False

print(withWild("?????","daily"))
