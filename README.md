# Tema Intermediara - Python (Anul 2)

Rezolvare pentru tema de parcurs la disciplina Python, realizata in cadrul echipei **E69**.

## Parametrii calculati
* **X = 5** (numarul de litere din prenume) -> `X % 6 = 5`
* **Y = 8** (numarul de litere din numele de familie) -> `Y // 5 = 1` manager, `Y // 6 = 1` task

## Structura proiectului
* `employee.py` - Contine clasa de baza `Employee` si clasa derivata `Manager` (Problema 1).
* `grafice.py` - Importa datele din `data.csv` si genereaza graficele cerute (Problema 2).
* `data.csv` - Setul de date folosit pentru vizualizare.
* `requirements.txt` - Lista pachetelor Python necesare.

## Instalare si rulare (Prerequisites & Run)

1. Crearea si activarea mediului virtual:

    python -m venv venv
    venv\Scripts\activate

2. Instalarea dependentelor:

    pip install -r requirements.txt

3. Rularea problemelor (din directorul radacina al proiectului, unde se afla si `data.csv`):
   * **Problema 1:** `python employee.py`
   * **Problema 2:** `python grafice.py`

## Detalii de implementare

### Problema 1 (`employee.py`)
* Am creat clasa `Manager(Employee)` cu variabila de clasa `mgr_count = 0` pentru numararea instantelor create.
* Constructorul `__init__` preia `name, salary, task, position, department`, apeleaza `super().__init__(name, salary)` si actualizeaza dictionarul `self.tasks` cu task-urile primite.
* Deoarece `X % 6 == 5`, am suprascris metoda `display_employee()` in `Manager` pentru a afisa doar valorile task-urilor (`list(self.tasks.values())`).
* La final am apelat `display_employee()` pe instantele create si am afisat `empCount` atat prin instanta de tip `Employee`, cat si prin cea de tip `Manager`.

### Problema 2 (`grafice.py`)
* Am citit fisierul `data.csv` cu `pandas.read_csv()`.
* Am generat 3 grafice separate folosind `DataFrame.plot()` si `matplotlib.pyplot.show()`:
  1. Toate inregistrarile pentru coloanele `Durata`, `Puls`, `MaxPuls`, `Calorii`.
  2. Primele 5 inregistrari (`head(5)`) pentru `Durata`, `Puls`, `Calorii`.
  3. Ultimele 8 inregistrari (`tail(8)`) pentru `Durata` si `Puls`, configurate conform regulii `X % 6 == 5` cu culorile verde si albastru (`color=['green', 'blue']`) si marker diamant (`marker='D'`).

## Referinte
* Materialele de curs si laborator (clasa `Employee`, fisierul `data.csv`)
* Documentatia Pandas (`DataFrame.plot`, `head`, `tail`): https://www.w3schools.com/python/pandas/default.asp
* Documentatia Matplotlib (culori si markeri): https://www.w3schools.com/python/matplotlib_intro.asp