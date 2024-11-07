'''Write a list comprehension to print a list which contains the multiplication table of a
user entered number.'''

try:
    n = int(input("Enter a number: "))
    mul_list = [n*i for i in range(1,11)]
    print(mul_list)
except Exception as e:
    print("please enter an integar number")
