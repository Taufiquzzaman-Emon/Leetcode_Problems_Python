'''Override the __len__() method on vector of problem 5 to display the dimension of the
vector.'''

class Vector:
    def __init__(self, n, components):
        if len(components) != n:
            raise ValueError(f"Vector must have exactly {n} components.")
        self.components = components
        self.n = n  # n number of dimensions

    # Overload the + operator for vector addition
    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Vectors must have the same dimensions to add.")
        added_result = []
        for i in range(self.n):
            added_result.append (self.components[i] + other.components[i] )
        return Vector(self.n, added_result)
    def __len__(self):
        return self.n

    def __mul__(self, other):
        if self.n != other.n:
            
            raise ValueError("Vectors must have the same dimensions to add.")
        added_result = []
        for i in range(self.n):
            added_result.append (self.components[i]*other.components[i] )
        return Vector(self.n, added_result)
    # String representation of the vector
    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

# Input for the number of dimensions
n = int(input("Enter the number of dimensions (n): "))

# Input for the first vector
components1 = list(map(int, input(f"Enter {n} components of the first vector separated by spaces: ").split()))
v1 = Vector(n, components1)

# Input for the second vector
components2 = list(map(int, input(f"Enter {n} components of the second vector separated by spaces: ").split()))
v2 = Vector(n, components2)

# Perform vector addition
sum_vector = v1 + v2
mul_vector = v1*v2

# Output results
print(f"Sum of vectors: {sum_vector}")
print(f"Mul of vectors: {mul_vector}")
print(f"Length of the vector1 is: {len(v1)}D and Length of vector2 is also {len(v2)}D")
