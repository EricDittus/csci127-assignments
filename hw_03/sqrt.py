import random
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
