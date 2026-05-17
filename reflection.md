1. Exceptions -> Not knowing exception names

Errors:
1.
Traceback (most recent call last):
  File "C:\Users\User\OneDrive\Desktop\student_data_explorer\main.py", line 6, in <module>
    data = dataset.load()
  File "C:\Users\User\OneDrive\Desktop\student_data_explorer\src\models.py", line 27, in load
    raise DataError(f"File not found: {self.path}")
src.exceptions.DataError: File not found: data/students.csv