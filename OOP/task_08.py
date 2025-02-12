class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)

    @classmethod
    def from_string(cls, employee_str):
        name, salary = employee_str.split(", ")
        return cls(name, float(salary))

    @staticmethod
    def is_high_salary(salary):
        return salary > 100000

employee = Employee.from_string("Alice, 120000")
print(f"Employee name: {employee.name}, Salary: {employee.salary}")
print("Is the salary high?", Employee.is_high_salary(employee.salary))
