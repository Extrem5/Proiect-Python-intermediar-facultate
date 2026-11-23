# Documentație Temă Python — Stoica Dragoș Gabriel (Echipa E69)

## 1. Prerequisites & Run (Cerințe și rulare)

**Prerequisites:**
* Este necesar un interpretor Python 3 (ex. Python 3.10+) sau mediul local MSYS2 / MinGW64.
* Pentru rularea Problemei 2 și a testelor de la Problema 1, trebuie instalate bibliotecile `pandas`, `matplotlib` și `pytest` folosind comanda:
  `pip install pandas matplotlib pytest` *(ele pot fi instalate și prin managerul de pachete `pacman`)*.
  * Pentru Problema 1 (`pytest`):
    `C:\msys64\usr\bin\pacman.exe -S --noconfirm mingw-w64-ucrt-x86_64-python-pytest`
  * Pentru Problema 2 (`pandas` și `matplotlib`):
    `C:\msys64\usr\bin\pacman.exe -S --noconfirm mingw-w64-ucrt-x86_64-python-pandas mingw-w64-ucrt-x86_64-python-matplotlib`

**Run:**
  *Pentru problema 1: 
  `cd Stoica.Dragos\problema1`
  `python employee.py`
  *Pentru rularea testelor: 
  `pytest`/`pytest test_employee.py`(ambele comenzi sunt functionale,testele pentru pytest se ruleaza in general exclusiv prin comanda `pytest`)
  *Pentru problema 2: 
  `cd Stoica.Dragos\problema2`
  `python grafice.py` (fisierul data.csv trebuie sa se afle in acelasi director cu grafice.py)

  ## 2.Explicatia Rezolvarii

Calculul parametrilor personali pentru **Stoica Dragoș Gabriel**:
* `X = 13` (numărul de litere din prenumele *Dragoș* + *Gabriel*: 6 + 7) $\Rightarrow$ `X % 6 == 1`
* `Y = 6` (numărul de litere din numele de familie *Stoica*)

### Problema 1 (`employee.py` și `test_employee.py`)
* Am creat clasa `Manager(Employee)` cu variabila de clasă `mgr_count = 0` pentru numărarea instanțelor create.
* Constructorul `__init__` preia `name, salary, task, position, department`, apelează `super().__init__(name, salary)` și actualizează dicționarul `self.tasks` cu task-ul primit prin `self.modify_task(task)`.
* Deoarece `X % 6 == 1`, am suprascris metoda `display_employee()` în `Manager` pentru a afișa exclusiv numele angajatului (`print("Name: ", self.name)`).
* Conform parametrilor personali, am creat `Y / 5 = 1` instanță de tip `Manager` (cu `Y / 6 = 1` task, poziția `"Team Lead"` și departamentul `"E69_Stoica_Cojocaru"`).
* La final am apelat `display_employee()` pe instanțele create și am afișat `emp_count` atât prin instanța de tip `Employee`, cât și prin cea de tip `Manager`.
* Pentru testarea unitară (`test_employee.py`), am implementat 4 teste cu `pytest` care verifică inițializarea unui `Manager`, afișarea numelui prin `display_employee()`, contoarele `emp_count` / `mgr_count` și modificarea salariului/task-urilor.

### Problema 2 (`grafice.py`)
* Am citit fișierul `data.csv` cu `pd.read_csv("data.csv")`.
* Am generat 3 grafice separate folosind `DataFrame.plot()` și `plt.show()` după fiecare grafic:
  1. Toate înregistrările pentru coloanele `Durata`, `Puls`, `MaxPuls`, `Calorii`.
  2. Primele 13 înregistrări (`head(13)`) pentru `Durata`, `Puls`, `Calorii`.
  3. Ultimele 6 înregistrări (`tail(6)`) pentru `Durata` și `Puls`, configurate conform regulii `X % 6 == 1` cu culorile albastru și galben (`color=["blue", "yellow"]`) și marker triunghi în sus (`marker="^"`).

  ## 3.Referinte bibliografice

  -Materiale de curs( Curs3_GIT1.pdf,Curs4_GIT2.pdf,clasa Employee,data.csv)
  -Documentatie Pandas:https://www.w3schools.com/python/pandas/default.asp
  -Documentatie Inheritance:https://www.w3schools.com/python/python_inheritance.asp
  -Documentatie Matplotlib:https://www.w3schools.com/python/matplotlib_intro.asp
  -Documentatie Pytest:https://docs.pytest.org/en/stable/




