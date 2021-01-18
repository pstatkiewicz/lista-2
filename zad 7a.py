def Fibonacci(n):
    if n<1:
        return 0
    number1,number2=0,1
    print(number2)
    for i in range(n-1):
          result=number1+number2
          number1=number2
          number2=result
          print(result)
n=int(input("Podaj ilość liczb, która ma wystąpić w ciągu: "))
print(Fibonacci(n))
