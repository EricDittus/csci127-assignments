#Eric Dittus
def filterodd(l):
    i=0
    oddlist=[]
    while i<=len(l)-1:
        if l[i] % 2 is not 0:
            oddlist.append(l[i])
        i = i + 1
    return oddlist
        
print(filterodd([1,2,3,4,5,6,7,8]))

def mapsquare(l):
    i=0
    squaredlist=[]
    while i<=len(l)-1:
        squaredlist.append(l[i]*l[i])
        i = i + 1
    return squaredlist

print(mapsquare([4,2,5,3,5]))
