import pytest
from employee import Employee, Manager


def test_creare_manager():
    mgr = Manager("Ana", "9000", {"TaskA": "New"}, "QA", "Echipa69_Cojocaru_Stoica")
    
    # Verificam daca atributele au fost setate corect
    assert mgr.name == "Ana"
    assert mgr.salary == "9000"
    assert mgr.position == "QA"
    assert mgr.department == "Echipa69_Cojocaru_Stoica"
    assert mgr.tasks == {"TaskA": "New"}


def test_modificare_task():
    mgr = Manager("Vlad", "8500", {"Task1": "New"}, "Dev", "Echipa69_Cojocaru_Stoica")
    
    # Folosim metoda mostenita din Employee pentru a schimba statusul
    mgr.modify_task("Task1", "Completed")
    assert mgr.tasks["Task1"] == "Completed"
    
    # Adaugam un task nou fara status (ar trebui sa ia implicit "New")
    mgr.modify_task("Task2")
    assert mgr.tasks["Task2"] == "New"


def test_afisare_display_employee_pentru_manager(capsys):
    # capsys este o unealta integrata in pytest care "captureaza" tot ce se afiseaza cu print()
    mgr = Manager("Elena", "9500", {"T1": "In progress", "T2": "Done"}, "Scrum Master", "Echipa69_Cojocaru_Stoica")
    
    mgr.display_employee()
    
    # Citim ce a afisat functia in consola
    output = capsys.readouterr().out
    assert "['In progress', 'Done']" in output