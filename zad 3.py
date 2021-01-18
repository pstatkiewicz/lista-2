def signs_from_position(sign,position,string):
    if len(sign)!=1:
        return "Błąd"
    if position>=len(string):
        return "Błąd"
    lista=[]
    for i in range(position,len(string)):
        if string[i]==sign:
            lista.append(i)
    return lista
string=input("Podaj łańcuch znaków: ")
sign=input("Podaj znak do znalezienia: ")
position=int(input("Podaj miejsce od której pozycji szukać: "))
print("Znak znajduje się na",signs_from_position(sign,position,string),"pozycjach")
