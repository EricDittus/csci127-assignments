def countApplesAndOranges(s,t,a,b,apples,oranges):
    num_apples=0
    num_oranges=0
    for d in apples:
        d = a + d
        if s<=d and d<=t:
            num_apples +=1
    for d in oranges:
        d = b + d
        if t>=d and s<=d:
            num_oranges +=1
    print(num_apples)
    print(num_oranges)
    
countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])
countApplesAndOranges(-2,-5,-6,6,[-2,3,10,15],[11,-2])    
