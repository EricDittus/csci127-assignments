import random
#could not figure it out, but found this online
#def mysqrt(x):
#    epsilon = 0.01
#    left= 0
#    right = x
#    guess = (right+left)/2.0
#    while abs(guess**2 - x) > epsilon:
#        if guess**2 < x:
#            left = guess
#        else:
#            right = guess
#        guess = (right+left)/2.0
#    print (guess)
def mysqrt(square):
    output=0
    guess=0
    i=0
    if ((square - output*output)/100) > 0.01:
        while square != output*output:
            guess = random.randint(1,square)
            output = (guess + (square/guess))/2
            print (output)
            i = i + 1
        
    return output
