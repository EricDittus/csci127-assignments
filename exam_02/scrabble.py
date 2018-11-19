def score(w):
    score = 0
    i = 0
    while i < len(w):
        if w[i] in "aeioulnrstAEIOULNRST":
            score = score + 1
        if w[i] in "dgDG":
            score = score + 2
        if w[i] in "bcmpBCMP":
            score = score + 3
        if w[i] in "fhvwyFHVWY":
            score = score + 4
        if w[i] in "kK":
            score = score + 5
        if w[i] in "jxJX":
            score = score + 8
        if w[i] in "qzQZ":
            score = score + 10
        i +=1
    return score
print(score("hello"))
print(score("Okaayyayjhk"))
print(score("ZZZZABEIss"))
