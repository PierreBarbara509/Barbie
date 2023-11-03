chenn = "Nan yon chenn karaktè, mete tout karaktè yo an miniskil."
chenn_miniskil = chenn.lower()
print(chenn_miniskil)

#Koupe chenn nan tout kote ki gen espas:
chenn = "Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas."
mots = chenn.split()
print(mots)

#Mete tout premye lèt chak mo an majiskil:
chenn = "Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil."
mots = chenn.split()
mots_majiskil = [mot.capitalize() for mot in mots]
resultat = " ".join(mots_majiskil)
print(resultat)

#Ranplase tout karaktè "a" pa "@":
chenn = "Ranplase tout karaktè a pa @"
chenn_modifikasyon = chenn.replace('a', '@')
print(chenn_modifikasyon)

#Mete yon chenn devan dèyè, ak l an majiskil:
chenn = "Ayiti"
chenn_modifikasyon = chenn.upper() + chenn.lower()
print(chenn_modifikasyon)
#Afiche endeks premye karaktè "a" nan yon chenn:
chenn = "Ayiti kapab avanse"
endeks = chenn.index('a')
print(endeks)


#Afiche total tout endeks karaktè "a" nan yon chenn:
chenn = "Ayiti kapab avanse"
endeks = [i for i, char in enumerate(chenn) if char == 'a']
total_endeks = len(endeks)
print(total_endeks)

#Kreye yon lis ki gen endeks tout karaktè "a" nan yon chenn (sèlman a miniskil):
chenn = "Ayiti kapab avanse"
endeks = [i for i, char in enumerate(chenn) if char == 'a']
endeks_miniskil = [i for i in endeks if chenn[i].islower()]
print(endeks_miniskil)

#Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen:
chenn = "Retire tout espas yo."
chenn_sans_espas = chenn.replace(" ", "")
kantite_karaktè = len(chenn_sans_espas)
print("chenn_sans_espas, kantite_karaktè")




