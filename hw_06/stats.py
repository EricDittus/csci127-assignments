'''
Created by SAM EBERSOLE and ERIC DITTUS
'''


import random

def create_random_list():
    i = 0
    list = []
    while i <= 100:
        list.append(random.randint(0,10))
        i += 1
    return list
        
def find_largest (list):
    largest = 0
    for item in list:
        if item > largest:
            largest = item
    return largest

def count_occurance (num, list):
    count = 0
    for item in list:
        if item == num:
            count += 1
    return count

list = create_random_list()
print(find_largest(list))
print(count_occurance(6, list))
