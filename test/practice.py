def fizzbuzz(max_num):
    i = 1
    while i <= max_num:
        if (i%5==0):
          if (i%3==0):
            print("FIZZBUZZ")
          else:
            print("buzz")
        if i % 3 == 0:
          if (i%5!=0):
            print("fizz")
        if (i%5!=0) and (i%3!=0):
          print(i)
        i += 1

print(fizzbuzz(1000))


def didit(name):
    print(name + " completed this assignment")

print(didit("Jerry"))
