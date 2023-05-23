l1 = [1,2,3,2,4,3,4,4,4,5]
def odds(l1):
    r = 0
    for x in l1:
        r  = r ^ x 
    print(r)
odds(l1)
