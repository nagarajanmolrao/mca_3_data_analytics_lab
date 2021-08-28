#Write a Python program to perform linear search

size = int(input("Enter the number of elements:\n"))
arr = []
for i in range(0, size):
    ele = int(input("Enter "+str(i)+" element: "))
    arr.append(ele)

searchElement = int(input("Enter the search element:\n"))
if searchElement in arr:
    print("Element found at", arr.index(searchElement)+1, "position")
else:
    print("Element not found in the list !")