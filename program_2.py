#Write a Python program to insert an element into a sorted list

size = int(input("Enter the number of elements:\n"))
arr = []
for i in range(0, size):
    ele = int(input("Enter "+str(i)+" element: "))
    arr.append(ele)

arr.sort()
element = int(input("Enter the element to be inserted: "))
for i in range(len(arr)):
    if arr[i] > element:
        break
arr = arr[:i] + [element] + arr[i:]
print(arr)