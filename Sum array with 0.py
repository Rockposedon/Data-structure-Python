size = int(input())
numbers = list(map(int,input().split()))
sublist = []
result = 0
for i in range(0,size+1):
    for j in range(i+1,size+1):
        sublist.append(numbers[i:j])
for i in sublist:
    if sum(i)==0:
        print("yes")
        print(i)
        
        result = 1
if result == 0:
    print("no")