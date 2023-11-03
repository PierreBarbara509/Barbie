#Barbara
import random
import pickle

nom=(input("Antre nonw"))

if not nom.islower():
    nom=(input("nonw antre a pa valid"))
if''in nom :
    nom=(input("ou dwe antre yon non san espas,reeseye"))
    
    print("Bonjour{nom},bienvini nan jwet la")
    
    nonb_kache=random.randit[0,10]
    
    chans_kache=3
    
    
    while true:
       while chans_kache>0:
    try:
        mesaj=int(input("antre yon nonb nan [0,10].ou gen{chans kache}chans:")) 
        
        if mesaj<0 or mesaj>10
        print("nonb lan dwe nan enteval[0,10]")   