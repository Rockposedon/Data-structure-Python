def summ1(n):
    print(n*(n+1)/2)
n = int(input("enter the value :"))
summ1(n)

#------------------------------------#
def summ2(n):
    sum = 0
    i = 1
    while i<=n:
        sum = sum+i
        i = i+1
        print(sum)
summ2(n)