def encode(stringy):
    i = 0
    new_list = []
    while i < len(stringy):
        count=1
        curent_letter = stringy[i]
        j = 0
        while stringy[i] == stringy[i+1]:
            item=[]
            count += 1
            item[0]=curent_letter
            item[1]=counts
            new_list[j] = item
            j+=1
            i+=1
        
            new_list[j]=item
    return new_list
print(encode("abbaaacddaaa"))
print(encode("abcd"))
print(encode("ooooooo"))

def decode(new_list):
    word = ""
    i = 0
    while i < len(new_list):
        item =new_list[i]
        j = 0
        while j <= item[1]:
            word = "" + item[0]
            j +=1
        i += 1
print(decode(encode("abbaaacddaaa")))
print(decode(encode("yahhyayayay")))
