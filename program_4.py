# Implement a python program to demonstrate
# 1)Importing Datasets 2)Cleaning the data 3) Data frame manipulation using NumPy

import numpy as np

with open("supportFiles/dataForProgram4.txt", "r") as fp:
    print(np.loadtxt(fp, delimiter=',', dtype=int))


