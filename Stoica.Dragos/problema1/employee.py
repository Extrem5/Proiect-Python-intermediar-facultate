class Employee:
    """Common base class for all employees"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}  # dict with task_name:status
        Employee.emp_count += 1

    def display_emp_count(self):
        """Displays the number of employees"""
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.emp_count -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    """Clasa Manager care mosteneste clasa Employee"""
    mgr_count = 0

    def __init__(self, name, salary, task, position, department):
        super().__init__(name, salary)
        self.modify_task(task)  # Adaug primul task in dictionarul self.tasks (Y/6 = 6/6 = 1 task)
        self.position = position
        self.department = department
        Manager.mgr_count += 1

    def display_employee(self):
        # Pentru X = 13 (Dragos Gabriel), X % 6 == 1 => afisez doar numele angajatului
        print("Name: ", self.name)

    def __del__(self):
        super().__del__()
        Manager.mgr_count -= 1


if __name__ == "__main__":
    # Obiect din clasa de baza Employee
    emp1 = Employee("Alin", 5000)

    # X = 13 (Dragos Gabriel), Y = 6 (Stoica)
    # Y / 5 = 6 / 5 = 1 => creez 1 obiect Manager
    # Y / 6 = 6 / 6 = 1 => fiecare manager are 1 task
   
    mgr1 = Manager(
        name="Stoica Dragos Gabriel",
        salary=9500,
        task="QA",
        position="Team Lead",
        department="E69_Stoica_Cojocaru"
    )

    print(" Afisare detalii Manager (doar numele, deoarece X%6 == 1) ")
    mgr1.display_employee()

    print("\n Afisare detalii Employee ")
    emp1.display_employee()

    print("\n Afisare emp_count ")
    print("emp_count accesat prin instanta Employee:", emp1.emp_count)
    print("emp_count accesat prin instanta Manager:", mgr1.emp_count)