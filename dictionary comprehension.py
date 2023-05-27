l1 = [1,12,1,2,3,4,4,5,6,77,7,7,8,7,65,4,4,32,2,1,10]
l2 = ['a','b','c','d','e','f','g','h','i','k','j','k']
d1 = {x:x**3 for x in l1}
print(d1)
# --------------
d2 = dict(zip(l1,l2))
print(d2)
#inverting the dictionary 
da = {101:'p',102:'a',103:'r'}
dB = { v:k for(k,v) in da.items() }
print(dB)

