class EmployeeDetails:
    def __init__(self, e_id, e_name, sal):
        # Get employee details using constructor
        self.e_id = e_id
        self.e_name = e_name
        self.sal = sal

    def __str__(self):
        # Another constructor in python which will only return the string values.
        # It will get invoked when object is created
        return self.e_name

    def display_emp_details(self):
        print("Employee ID      : ", self.e_id)
        print("Employee Name    : ", self.e_name)
        print("Employee ID      : ", self.sal)


ed = EmployeeDetails(101, "XYZ", 9000.9)
ed.display_emp_details()
print(ed)
