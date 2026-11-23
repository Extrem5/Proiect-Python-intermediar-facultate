import pytest
from employee import Employee, Manager


def test_creare_manager():
    mgr = Manager("Cojocaru Tudor", 9500, "QA", "Team Lead", "E69_Stoica_Cojocaru")
    assert mgr.name == "Cojocaru Tudor"
    assert mgr.salary == 9500
    assert mgr.position == "Team Lead"
    assert mgr.department == "E69_Stoica_Cojocaru"
    assert mgr.tasks == {"QA": "New"}


def test_display_employee_manager(capsys):
    # Pentru X = 13 (X % 6 == 1), display_employee trebuie sa afiseze doar numele
    mgr = Manager("Radu", 9500, "AI", "Developer", "E69_Stoica_Cojocaru")
    mgr.display_employee()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Name:  Radu"


def test_contoare_angajati_si_manageri():
    initial_emp = Employee.emp_count
    initial_mgr = Manager.mgr_count

    mgr = Manager("Ady", 9500, "Embedded", "Engineer", "E69_Stoica_Cojocaru")
    assert Employee.emp_count == initial_emp + 1
    assert Manager.mgr_count == initial_mgr + 1

    del mgr
    assert Employee.emp_count == initial_emp
    assert Manager.mgr_count == initial_mgr


def test_modificare_salariu_si_task():
    mgr = Manager("Ady", 9500, "Dev", "Team Lead", "E69_Stoica_Cojocaru")
    mgr.update_salary(11000)
    mgr.modify_task("Dev", "Done")
    assert mgr.salary == 11000
    assert mgr.tasks["Dev"] == "Done"