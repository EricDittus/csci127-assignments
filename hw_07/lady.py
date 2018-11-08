def happy_ladybugs(L):
    if '_' in L:
        L = L.replace('_','')
      
        repetition = {}
        
        for i in L:
            repetition.setdefault(i,0)
            repetition[i] += 1
    
        for i in repetition.values():
            if i < 2:
                return 'NO'
        
        return 'YES'

    elif Full(L):
        return 'YES'
    
    else:
        return 'NO'
    
    
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
