#Eric Dittus
import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l
print(build_random_list(5,100))

def locate(l,value):
# i=0
# found_index = -1
# while i < len(l):
#   print(value,i,l[i])
#   if l[i] == value:
#       found_index = i
#       break
#   i += 1
# return found_index
    if value in l:
        return l.index(value)
    else:
        return -1
print(locate([5,7,8,9,4,6],8))


def count(l,value):
    i=0
    count_value=0
    while i< len(l):
        if l[i]==value:
            count_value += 1
        i += 1
    return count_value
print(count([1,1,1,1,2,5,7],1))

def reverse(l):
    l_new=[]
    i=len(l)-1
    while i>=0:
        l_new.append(l[i])
        i-=1
    return l_new
print(reverse([1,2,3,4,5,6]))

def isIncreasing(l):
    i=0
    less_than_counter=0
    #This will count how many times the previous value is
    #less than the one after it. If the correct
    #amount is met, this program will return true
    while i<=len(l)-2:
        if l[i]<l[i+1]:
            less_than_counter+=1
        else:
            return False
        i+=1
    if less_than_counter==len(l)-1:
        return True
print(isIncreasing([1,3,5,6,8,10]))
print(isIncreasing([4,3,6,3]))
    
def palindrome(l):
    index=0
    mirror_index=-1
    pal_check=0
    while index<= len(l)/2: #should work for odd and even lengths
        if l[index]==l[mirror_index]:
            pal_check+=1
        else:
            return False
        index+=1
        mirror_index-=1
    if (len(l)%2 is 0) and pal_check==len(l)/2:
        return True
    elif (len(l)%2 is not 0) and (pal_check>(len(l)/2-1)):
        return True
print(palindrome('eve'))
print(palindrome('thaht'))


            
    
