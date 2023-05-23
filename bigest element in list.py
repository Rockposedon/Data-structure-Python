l1 = []
x = 10
for i in range(99,1001):
    l1.append(i)
print(l1)
g = l1[0]
for i in range(1,len(l1)):
    if g < l1[i]:
        g = l1[i]    
print("greatest : ", g)