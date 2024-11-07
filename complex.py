''' Write a class ‘Complex’ to represent complex numbers, along with overloaded
operators ‘+’ and ‘*’ which adds and multiplies them.'''

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __add__(self,c2):
        return Complex (self.r+c2.r,self.i+c2.i)
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imaginary_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return f"{self.r}+{self.i}i"
# Input for the first complex number
real1 = int(input("Enter the real part of the first complex number: "))
imaginary1 = int(input("Enter the imaginary part of the first complex number: "))
c1 = Complex(real1, imaginary1)

# Input for the second complex number
real2 = int(input("Enter the real part of the second complex number: "))
imaginary2 = int(input("Enter the imaginary part of the second complex number: "))
c2 = Complex(real2, imaginary2)

# Perform addition and multiplication of the complex numbers
sum_result = c1 + c2
mul_result = c1*c2

print(sum_result)
print(mul_result)