import time
def signs_counter(sign,string):
    if len(sign)>1:
        return "Błąd"
    counter=string.count(sign)
    return counter,sign
string=input("Podaj łańcuch znaków: ")
sign=input("Podaj znak do znalezienia: ")
start=time.time()
result=signs_counter(sign,string)
end=time.time()
time=end-start
print("Jest",result,"w tym łańcuchu")
print("Czas wykonania tego programu to",time)

