from functools import reduce
'''Write a program to find the maximum of the numbers in a list using the reduce
function.'''

l1 = [10,1001,1,5,50,33,9,100]

def greater(a,b):
    if a>b:
        return a
    return b

great = reduce(greater,l1)
print(great)

