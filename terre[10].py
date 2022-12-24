from math import *
def premier (a):
    N=int(sqrt(a))
    compteur=0
    for i in range (1,N+1):
        if a%i == 0 :
            compteur=compteur+1
    if compteur == 1: #car 1 divise tous les éléments
        print(a , " est premier")
    else:
        print(a , " n'est pas premier")

premier(11)# Terre
