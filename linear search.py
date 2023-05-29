def search(a,x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

a = [1,2,6,4,5,6,7,8,9,11]
number = int(input())
result = search(a,number)
if result != -1:
    print(f"target number {number} found at index {result}")
else : 
    print(f"target number {number} not found at index {result}")
    