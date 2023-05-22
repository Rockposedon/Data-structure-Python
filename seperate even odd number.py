l1 = []
for i in range(1,21):
    l1.append(i)
print(l1)
def oddeven(l1):
    even = []
    odd = []
    for x in l1:
        if x%2 == 0 :
            even.append(x)
        if x%2 != 0:
            odd.append(x)
    print(even)
    print(odd)
        
oddeven(l1)
