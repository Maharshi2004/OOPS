# Create a class Employee
# Create private variables:
# __salary
# __designation
# Add method set_salary(salary)
# Salary should be greater than 0
# Prevent invalid updates
# Add method get_salary()
# Return salary
# Add method set_designation(role)
# Allow only specific roles (e.g., "Manager", "Developer", "HR")
# Add method get_designation()
# Return designation
# Add method increment_salary(percent)
# Increase salary based on percentage
# Percentage should not exceed 30%
# Do not allow direct access to salary or designation from outside the class

class Employee:
    def __init__(self):
        self.__salary = 0
        self.__designation = None
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            print("Salary set successfully")
        else:
            print("Salary must be greater than 0")
    def get_salary(self):
        return self.__salary
    def set_designation(self, role):
        allowed_roles = ["Manager", "Developer", "HR"]
        if role in allowed_roles:
            self.__designation = role
            print("Designation set successfully")
        else:
            print("Invalid role! Allowed roles:", allowed_roles)
    def get_designation(self):
        return self.__designation
    def increment_salary(self, percent):
        if 0 < percent <= 30:
            increment = (self.__salary * percent) / 100
            self.__salary += increment
            print("Salary incremented successfully")
        else:
            print("Increment percentage should be between 0 and 30%")
emp = Employee()
salary = int(input("Enter salary: "))
emp.set_salary(salary)
role = input("Enter designation (Manager/Developer/HR): ")
emp.set_designation(role)
print(emp.get_salary())
print(emp.get_designation())
percent = float(input("Enter increment percentage: "))
emp.increment_salary(percent)
print(emp.get_salary())