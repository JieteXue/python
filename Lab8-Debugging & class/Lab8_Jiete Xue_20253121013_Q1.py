class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department
    
    def assign_department(self, new_department):
        """Change the department of an employee"""
        self.department = new_department
    
    def calculate_salary(self, hours_worked):
        """
        Calculate salary with overtime if hours worked > 50
        Overtime formula: (hours_worked - 50) * (salary / 50)
        """
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.salary / 50)
            total_salary = self.salary + overtime_amount
        else:
            total_salary = self.salary
        
        return total_salary
    
    def print_employee_details(self):
        """Print all details of an employee"""
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Base Salary: ${self.salary:,.2f}")
        print(f"Department: {self.department}")
        print("-" * 30)



if __name__ == "__main__":
    employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
    
    # Change the departments of employee1 and employee4
    employee1.assign_department("OPERATIONS")
    employee2.assign_department("SALES")
    
    # Now calculate the overtime of the employees who are eligible:
    employee1.calculate_salary(52)
    employee2.calculate_salary(60)
    
    print("Updated Employee Details:")
    employee1.print_employee_details()
    employee2.print_employee_details()