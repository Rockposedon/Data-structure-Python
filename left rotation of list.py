l1 = [1,2,3,4,55,66,76,87,98,100,10022]
l1.append(l1.pop(0))
print(l1)
# -------------------
d = 3 
l2 = l1[d:] + l1[:d]
print(l2)
# -------------------
d=4
def lr(l1,d):
    for i in range(0,d):
        l1.append(l1.pop(0))
lr(l1,d)
print(l1)