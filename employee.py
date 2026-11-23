##employee.py
## X=5 , Y=8 , Echipa E69


class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {} # dict with task_name:status
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

## Typical status(es) for tasks in companies
##    New - just created
##    Pending / Asigned - manager asigned it to an employee
##    In progress - employee still working on it
##    Completed /Done - finished succesfully
##    Rejected - just created
##    Deprecated - no longer relevant
##    Blocked - hit a roadblock, can no longer work on it
        
    def add_task(self, task_name):
        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
        
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    """Manager class, inherits from Employee"""
    mgr_count = 0
    def __init__(self, name, salary, task, position, department):
        super().__init__(name, salary)
        self.position=position
        self.department = department
        Manager.mgr_count += 1
        if task is not None:
           self.tasks.update(task)
    def display_employee(self):
        print("Tasks : ", list(self.tasks.values())) ## X==5
emp1=Employee("Alin","5000")
manager1 = Manager("Mihai", "10000", {"Task1": "New"}, "Team Lead", "Echipa69_Cojocaru_Stoica")
manager1.display_employee()
emp1.display_employee()
print("empCount pentru instanta Employee:", emp1.empCount)
print("empCount pentru instanta Manager:", manager1.empCount)