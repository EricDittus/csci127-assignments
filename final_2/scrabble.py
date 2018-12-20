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
print(canMakeWord("eerriin","eerie"))
print(canMakeWord("nope","okay"))
print(canMakeWord("wrong","right"))

def withWild(letters,word):
    count = 0
    i=0
    while i <= len(word)-1:
        if word[i] in letters:
            count += 1
            letters[letters.find(word[i])]==''

        if (word[i] not in letters) and ('?' in letters):
                letters[letters.find('?')]==''
                count += 1

        i+=1

    if count == len(word):
        return True
    else:
        return False

print(withWild("?????","daily"))
print(withWild("?utchg","gotchu"))
print(withWild("?utch?","gotchu"))
print(withWild("luck","okay"))
