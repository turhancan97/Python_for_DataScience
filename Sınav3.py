
def islem(x,y):
    A = [x,y]
    return A[0] + A[1]

islem(1,3)      


def islem(x, y):
    print(x - y)

islem(3,6)

A = "*A*"    
if type(A) == str:
    A = A.strip("*")
    print(A)
    

urun_fiyatlari = [19,29,39]
 
for i in urun_fiyatlari:
    if i >= 30:
        print(i/2)
    else:
        print(i*0)
        

def yazdir(metin):
    print(metin, "yazanlar")
 
yazdir("gelecegi")


def harf_say(x):
    len(x)
 
harf_say("Merhaba!")

a = [1,2,3]
b = []
for i in a:
    b.append(i**2)
b

a = [2,4,6,8]
for i in a:
    print(i**2)
    
    
A = 12    
if type(A) == str:
    A = A.strip("*")
    print(A)    
else:
    A  = "*" + str(A) + "*"
    print(A.strip())
    
    
liste = ["a","b","c"]
liste.reverse()
print(liste)

A = []

for i in [1,2,3,4]:
    A.append(i)

A[0]



sayilar = [10,20,30]
 
for i in sayilar:
    if i > 20:
        print(i/2)
        
        
        
sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        break
    print(i)
    
    
    
def mesaj():
    print("Merhaba!")    
    
mesaj()    


def islem(x, y):
    print(x + y)
 
islem(1,9)


def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
 
islem(4)