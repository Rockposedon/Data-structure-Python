l1 = []
for i in range(1,51):
    l1.append(i)
leng = len(l1)
print(leng)
print(l1)
def sum1(l1):
    sum = 0
    for x in l1:
        sum = sum+x
    average = sum/leng
    print("average = ", average)
    print(sum)
    
sum1(l1)