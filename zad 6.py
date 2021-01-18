def strings_comparison(string1,string2):
    mini=min(len(string1),len(string2))
    maxi=max(len(string1),len(string2))
    for i in range(mini):
        if string1[i]<string2[i]:
            print("Na",i,"pozycji pierwszy łańcuch ma mniejszy znak niż drugi łańcuch",string1[i],"<",string2[i])
        elif string1[i]>string2[i]:
            print("Na",i,"pozycji pierwszy łańcuch ma większy znak niż drugi łańcuch",string1[i],">",string2[i])
        else:
            print("Na",i,"pozycji łańcuchy mają ten sam znak",string1[i])
    i+=1
    if len(string1)>len(string2):    
        print("Reszta znaków nie ma porównania, ponieważ drugi łańcuch się skończył")
        print("Oto reszta znaków pierwszej pętli: ")
        while i<maxi:
            print(string1[i])
            i+=1
    elif len(string1)<len(string2):
        print("Reszta znaków nie ma porównania, ponieważ pierwszy łańcuch się skończył")
        print("Oto reszta znaków drugiej pętli: ")
        while i<maxi:
            print(string2[i])
            i+=1
    else:
        print("Oba łańcuchy się skończyły")
    return "Koniec porównania"
string1=input("Podaj pierwszy łańcuch znaków: ")
string2=input("Podaj drugi łańcuch znaków: ")
print(strings_comparison(string1,string2))
              
