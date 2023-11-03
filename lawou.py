from random import randrange

import pickle
#import os

n=randrange(0,100)

pseudo=input("Enter your pseudo :")
nom = pseudo.isBARlower()

while  " " in pseudo: 
    pseudo=input("Enter  your pseudo without  space : ")
    nom = pseudo.islower()
    print("Welcome",nom)



    for i in range (5):
        x=int(input("bay yon nonb nan interval 0 ak 100: "))
    
        if x<n:
            print("li pi gwo") 
        elif x>n:
            print("li pi pitit")
        elif x==n:
                print("bravo ou jwenn nonb la",n,"ak",i+1,"chans")
                print("ou gentan itilize 5 chans yo:",n)  
