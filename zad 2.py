def signs_in_string(sign,string):
    if len(sign)!=1:
        return "Błąd"
    lista=[]
    for i in range(len(string)):
        if string[i]==sign:
            lista.append(i)
    return lista
string=input("Podaj łańcuch znaków: ")
sign=input("Podaj znak do znalezienia: ")
print("Znak znajduje się na",signs_in_string(sign,string),"pozycjach")

    

