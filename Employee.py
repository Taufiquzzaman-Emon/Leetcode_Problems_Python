'''Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
which changes the value of increment based on the salary'''
class Employee:
    def __init__(self, salary, increment=0):
        # Ensure that the salary is not negative
        while salary < 0:
            print("Negative salary is not accepted. Please enter a valid salary.")
            salary = int(input("Enter the current salary again: "))
        self.salary = salary
        self.increment = increment

    @property
    def salary_after_increment(self):
        return self.salary * (1 + self.increment / 100)

    @salary_after_increment.setter
    def salary_after_increment(self, new_salary):
        # Ensure the new salary is not negative
        while new_salary < 0:
            print("New salary cannot be negative. Please enter a valid salary.")
            new_salary = int(input("Enter the new salary again: "))
        self.increment = ((new_salary / self.salary) - 1) * 100
        print(f"Your salary increment is {self.increment:.2f}%.")

# Input salary from the user
salary = int(input("Enter the current salary: "))

# Create Employee object
employee = Employee(salary)

# Display salary after increment
print(f"Salary after increment: {employee.salary_after_increment}")

# Input new salary to calculate increment
new_salary = int(input("Enter the new salary after increment: "))
employee.salary_after_increment = new_salary  # This will trigger the setter and calculate the increment





