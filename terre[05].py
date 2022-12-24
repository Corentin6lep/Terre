def RR(a,b):
    q=int(a/b)
    if (b != 0) and (q>=1):
        reste = a-b*q
        print("Le quotient de la division de ", a , "par ", b , "est de ", q)
        print("Le reste de la division de ", a , "par", b , " est de ", reste)

    else:
        print("erreur")

RR(2,3)# Terre
