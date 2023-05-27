def fun(n):
    if n == 1:
        return
    for i in range(n):
        print("Techritzy")
    fun(n/2)
n = float(input("enter value :"))    
fun(n)
