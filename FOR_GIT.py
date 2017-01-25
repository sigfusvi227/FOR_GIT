
print("Sigfús Már Viðarsson   FOR1TÖ05BU   Git Verkefni 25.1")

print("")
print("")
print("Dæmi 1")
print("Sláðu inn tvær tölur sem verða lagðar saman og svo margfaldaðar saman")
tala1 = int(input("Skrifaðu inn tölu eitt: "))
tala2 = int(input("Sláðu núna inn tölu tvö: "))
summan = (tala1)+(tala2)
margfoldun = tala1*tala2
print("")
print("Niðurstöðurnar verða þessar tölur...")
print("Summan er: " , (summan))
print("Margfölduninn verður: " , (margfoldun) )

print("Dæmi 1 Lokið")
print("")
print("")
print("")
print("Dæmi 2")
print("Sláðu inn nafnið þitt")
fornafn = input("Fornafn: ")
eftirnafn = input("Eftirnafn: ")
print ("Halló" , (fornafn) , (eftirnafn))
print("")
print("Dæmi 2 Lokið")
print("")
print("")
print("")

print("Dæmi 3")
print("Skrifaðu texta og ég mun segja þér hversu margir hástafir og lástafir eru í textanum.")
print("")
texti = input("Skrifaðu inn texta: ")
telhatala = 0
tellagtala = 0
tellagtalaeftir = 0
for x in range(len(texti)):
    if(texti[x].isalpha() and texti[x].isupper()):
        telhatala += 1
        if(x !=(len(texti)-1)):
            if(texti[x+1].islower()):
                tellagtalaeftir += 1
    if(texti[x].isalpha() and texti[x].islower()):
        tellagtala += 1
print ("Hversu margar hástafur: ",telhatala)
print ("Hversu margar lástafur: ",tellagtala)
print ("Hversu margar lástafur sem kemur eftir hástafi: ",tellagtalaeftir)
