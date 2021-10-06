# Implement a python program to demonstrate
# 1)Importing Datasets 2)Cleaning the data 3) Data frame manipulation using NumPy

import numpy as np

with open("supportFiles/grades.csv", "r", encoding="utf-8") as fp:
    print(np.genfromtxt(fp, delimiter=','))
