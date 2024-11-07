'''Write a program to filter a list of numbers which are divisible by 5.'''

l1 = [10,5,15,25,25,40,35,36,19,50]

def divideby5(n):
    if(n%5==0):
        return True
    return False
    
l = list(filter(divideby5,l1))

print(l)