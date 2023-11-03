import random
import pickle

#objectif jwet la
epsedo=(input("entrez votre pseudo"))
psedo=epsedo.replace("","")
if psedo.isalpha() and len(psedo)>=6 and(psedo)<=12:
    print("ou respecte condition an")
else:
    print("ou pa repectel")

# Kreye yon nonb kache
nonb_kache = random.randint(0, 100)

# Inisyalize kantite chans
kantite_chans = 10

while kantite_chans > 0:
    try:
        # Mande itilizatè a antre yon nonb nan entèval la
        guess = int(input(f"Antre yon nonb nan entèval [0, 100]. Ou gen {kantite_chans} chans: "))
        
        if guess < 0 or guess > 100:
            print("Nonb la dwe nan entèval [0, 100].")
            continue

        # Verifye si nonb la koresponn ak nonb kache a
        if guess < nonb_kache:
            print("Nonb la pi piti.")
        elif guess > nonb_kache:
            print("Nonb la pi gran.")
        else:
            print("BRAVO! Ou jwenn!")
            break

        # Diminye kantite chans
        kantite_chans -= 1

    except ValueError:
        print("Tanpri antre yon nonb valab.")

# Si itilizatè a pèdi
if kantite_chans == 0:
    print(f"Ou pèdi. Nonb kache a te {nonb_kache}.")
    
    # Enregistre skò itilizatè a nan yon fichye pickled
    with open('sko.pkl', 'wb') as sko_fichye:
        pickle.dump(kantite_chans, sko_fichye)
else:
    # Si itilizatè a jwenn, afiche skò li
    with open('sko.pkl', 'rb') as sko_fichye:
        sko_ansyen = pickle.load(sko_fichye)
    
    sko_nouvo = sko_ansyen + kantite_chans
    print(f"Skò ansyen: {sko_ansyen}, Nouvo skò: {sko_nouvo}")