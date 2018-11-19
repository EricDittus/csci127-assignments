def makeacronym(phrase):
    i = 0
    new_phrase=""
    phrase_list=phrase.split(" ")
    while i < len(phrase_list):
        next_word = phrase_list[i]
        new_phrase = new_phrase + next_word[0]
        i+=1
    print(new_phrase)
    return new_phrase

makeacronym("laugh out loud")
makeacronym("Read...fine manual")
makeacronym("In my humble opinion")
makeacronym("In my not so humble opion")
makeacronym("rsthghghSHBBDB HDBHs")
makeacronym(".........")
makeacronym("?!?/")
