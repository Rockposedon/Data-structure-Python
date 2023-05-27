l1 = []
x = 10
for i in range(99,98765):
    l1.append(i)
print(l1)
s = l1[0]
for i in range(1,len(l1)):
    if s > l1[i]:
        s=l1[i]
print(s)

