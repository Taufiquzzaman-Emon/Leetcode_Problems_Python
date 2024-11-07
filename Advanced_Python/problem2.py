'''Write a program to print third, fifth and seventh element from a list using enumerate
function.
'''
list = [1,2,3,4,5,6,7,8]
for index, item in enumerate(list):
    if index == 3 or index == 5 or index == 7:
        print(f"the number of Index {index} is {item}")

