A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def f(début):
    D=A.index(début)
    F=A.index("z")
    for i in range(D,F+1):
        print(A[i])
        
f("a")# Terre
