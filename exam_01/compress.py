#Eric Dittus
def compress_word(w):
    i=1
    j=2
    compressed=w[0]
    while i<=len(w)-2:
        letter = w[i:j]
        if letter not in "aeiouAEIOU":
            compressed = compressed + letter          
        i+=1
        j+=1
    if w[-1] not in "aeiouAEIOU":
        last=w[-1]
        compressed = compressed + last
        
    
    return compressed
print(compress_word("apple"))
print(compress_word("Special"))

def sentence(line):
    line_list = line.split()
    i=0
    while i<len(line_list):
        line_list[i]=compress_word(line_list[i])
        i+=1
    new_line= " ".join(line_list)
    return new_line
print(sentence("I like to eat apple pie."))
