def happy_ladybugs(L):
    items = uniqueitems(L)
    
    if '_' in items:
        items.remove('_')
        for i in items:
            count = 0
            for j in L:
                if i == j:
                    count += 1
            if count <= 1:
                return 'no'
        return 'yes'
    
    elif Full(L):
        return 'yes'
    
    else:
        return 'no'
    
    
def Full(L): 
    
    previous = L[0]
    consecutive = 1
    if len(L) == 1:
        return False
    
    for i in range(1,len(L)):
        if L[i] == previous:
            consecutive += 1
        elif consecutive > 1:
            if i == len(L) -1:
                return False
            previous = L[i]
            consecutive = 1
        else:
            return False
    return True


def uniqueitems(l):
    
    unique = []
    for i in l: 
        if i not in unique:
            unique.append(i)
    
    return unique


games = ['CBAABC','CCAABB','BBBBBB','_','A_B_AA','LFGG','ALACABAZLE',
         'SS_____SSAA_MMM']

for each in games:
    print(each,'  ',happy_ladybugs(each)) 
