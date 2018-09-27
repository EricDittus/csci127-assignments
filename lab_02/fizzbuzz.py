#Eric Dittus and Shanjida Kamal
def fizzbuzz(max_value):
    i = 1
    count = 0
    while i <= max_value:


        if (i % 5 ==0):
            if (i % 3 ==0):
                print ("FizzBuzz")
                count == count + 1
            else:
                print ( "Buzz")
        elif (i % 3==0):
            print ("Fizz")
        
    
        else:
            print (i)
        i=i+1
        
    return count
            
