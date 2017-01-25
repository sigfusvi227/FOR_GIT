
print("Sigfús Már Viðarsson   FOR1TÖ05BU   Git Verkefni 25.1")

print("")
print("")
print("Dæmi 1")
print("Sláðu inn tvær tölur sem verða lagðar saman og svo margfaldaðar saman") #Útskýring um dæmið
tala1 = int(input("Skrifaðu inn tölu eitt: ")) #Spyr um fyrstu tölu
tala2 = int(input("Sláðu núna inn tölu tvö: ")) #Spyr um tölu nr 2
summan = (tala1)+(tala2) #Summan við tölurnar
margfoldun = tala1*tala2 #Margfölduninn
print("")
print("Niðurstöðurnar verða þessar tölur...")
print("Summan er: " , (summan)) #útkoma summu
print("Margfölduninn verður: " , (margfoldun) ) #útkoma margföldun

print("Dæmi 1 Lokið")
print("")
print("")
print("")
print("Dæmi 2")
print("Sláðu inn nafnið þitt og forritið mun segja Halló (nafnið þitt)") #Útskýring um dæmið
fornafn = input("Fornafn: ") #spurt um fornafn
eftirnafn = input("Eftirnafn: ") #spurt svo um eftirnafn
print ("Halló" , (fornafn) , (eftirnafn)) #útkoma segir " Halló (Nafnið sem var sagt) "
print("")
print("Dæmi 2 Lokið")
print("")
print("")
print("")

print("Dæmi 3")
print("Skrifaðu texta og ég mun segja þér hversu margir hástafir og lástafir eru í textanum.") #Útskýring um dæmið
print("")
texti = input("Skrifaðu inn texta: ")
telhatala = 0
tellagtala = 0
tellagtalaeftir = 0
for x in range(len(texti)): #for in range fyrir textann
    if(texti[x].isalpha() and texti[x].isupper()): #Segjir hversu margar hátölur eru
        telhatala += 1 #hækkar um einn við hverja hátölu
        if(x !=(len(texti)-1)): #koma fyrir syndex error ef þú myndir enda með stórum staf
            if(texti[x+1].islower()): #talið þegar það kemur lítill stafur eftir stórum staf
                tellagtalaeftir += 1
    if(texti[x].isalpha() and texti[x].islower()):#Talið hversu margar lástafir eru
        tellagtala += 1
print ("Hversu margar hástafur: ",telhatala)
print ("Hversu margar lástafur: ",tellagtala)
print ("Hversu margar lástafur sem kemur eftir hástafi: ",tellagtalaeftir)
