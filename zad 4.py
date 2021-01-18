import time
def how_many_signs(sign,string):
    if len(sign)>1:
        return "Błąd"
    counter=0
    for i in range(len(string)):
        if string[i]==sign:
            counter+=1
    return counter,sign
string=input("Podaj łańcuch znaków: ")
sign=input("Podaj znak do znalezienia: ")
start=time.time()
result=how_many_signs(sign,string)
end=time.time()
time=end-start
print("Jest",result,"w tym łańcuchu")
print("Czas wykonania tego programu to",time)
