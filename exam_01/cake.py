def divide(A,B,u):
    People=1/(A/B)
    if People<1 and People!=0:
        People=1
    return People
print(divide(5,10,1))
print(divide(15,5,1))
