'''Store the multiplication tables generated in problem 3 in a file named Tables.txt.'''


n = int(input("Enter a number: "))
with open("tables.txt") as f:
    f= f.read()
with open("tables.txt","a") as f:
    
    mul_list = [n*i for i in range(1,11)]
    f.write(f"Multiplication Table of {n}: {str(mul_list)}\n")
print(mul_list)