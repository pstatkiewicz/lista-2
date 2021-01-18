def Fibonacci(n):
    if n<1:
        return 0
    elif n<3:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
n=int(input("Podaj ilość wyrazów ciągu: "))
for i in range(1,n+1):
    print(Fibonacci(i))
