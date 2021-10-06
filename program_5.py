# 5.Implement a python program to demonstrate the following using NumPy
# a)	Array manipulation, Searching, Sorting and splitting.
# b)	broadcasting and Plotting NumPy arrays

import numpy as np

npArray = np.random.randint(10, 100, (4, 4), dtype=int)


def arrayManipulation():
    global npArray
    npArray = npArray.T
    print("NumPy Array has been transposed")
    return


def arraySearch():
    global npArray
    key = int(input("Enter the search element: "))
    x, y = np.where(npArray == key)
    if len(x) == 0 or len(y) == 0:
        print("Key element not found in the dataset!")
        return
    else:
        print("key element found at \n",)
        for i in range(0, len(x)):
            print("[", x[i], ",", y[i], "]\n")
        print("position(s)")
        return


def arraySort():
    global npArray
    sort_choice = "-1"
    print("1. Sort Row wise\n2. Sort Column wise\n")
    while sort_choice not in "12":
        sort_choice = input("Enter your choice: ")
    sort_choice = int(sort_choice)
    if sort_choice == 1:
        npArray = np.sort(npArray, axis=0)
    else:
        npArray = np.sort(npArray, axis=1)
    return


def arraySplit():
    global npArray
    split_choice = "-1"
    print("1. Split Row wise\n2. Split Column wise\n")
    while split_choice not in "12":
        split_choice = input("Enter your choice: ")
    split_choice = int(split_choice)
    if split_choice == 1:
        print("Split array: \n")
        for i in np.vsplit(npArray, 2):
            print(i, end="\n")
    else:
        print("Split array: \n")
        for i in np.hsplit(npArray, 2):
            print(i, end="\n")
    return


def arrayBroadcast():
    global npArray
    b = np.random.randint(0, 10, (1, 4), dtype=int)
    print("Broadcast Array: ", b)
    npArray = npArray + b
    return


def arrayPlot():
    import matplotlib.pyplot as plt
    x = np.arange(1, 10)
    y = x * x
    plt.plot(x, y, color="blue")
    plt.show()
    return


choice = -1
while choice != 7:
    print("NumPy Array: \n\n", npArray)
    print("\n1. Array Manipulation\n2. Searching\n3. Sorting\n4. Splitting\n5. Broadcasting\n6. Plotting\n7. Exit\n\n")
    choice = int(input("Enter Choice: "))
    if choice in range(1, 8):
        if choice == 1:
            arrayManipulation()
        elif choice == 2:
            arraySearch()
        elif choice == 3:
            arraySort()
        elif choice == 4:
            arraySplit()
        elif choice == 5:
            arrayBroadcast()
        elif choice == 6:
            arrayPlot()
        else:
            print("Exiting...")
            exit(0)
    else:
        print("Please enter the correct option")
