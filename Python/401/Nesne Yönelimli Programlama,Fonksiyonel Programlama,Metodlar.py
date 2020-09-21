##Nesne Yönelimli Programlama

#Sınıf Nedir?

class VeriBilimci1():
    print("Bu bir sınıftır")
    
#Sınıf Özellikleri (Class Attributes)
    
class VeriBilimci():
    bolum = ""
    sql = "EVET"
    deneyim_yili = 0
    bilinen_diller = []

#Sınıf Özelliklerini erişmek
VeriBilimci.bolum
VeriBilimci.sql
    
#Sınıf Özeliklerini değiştirmek

VeriBilimci.sql= "Hayir"
VeriBilimci.sql
    
#Sınıf Örneklemesi

ali = VeriBilimci()
ali.sql
ali.deneyim_yili
ali.bolum
ali.bilinen_diller.append("Python") #Aliye python ekledik
ali.bilinen_diller

veli = VeriBilimci()
veli.sql
veli.bilinen_diller # Velide python biliyor çıkıyor ve bunu istemiyoruz.

#Örnek Özellikleri

class VeriBilimci():
    bildigi_diller = ["R","Python"]
    def __init__(self):
        self.bildigi_diller=[]
        
ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller.append("R")
veli.bildigi_diller
VeriBilimci.bildigi_diller

#Örnek Metodlar
class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum = ""
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)

ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
ali.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle #Hata Alır çünkü kişiye atamamız lazım

ali.dil_ekle("R")
ali.bildigi_diller

#Miras Yapıları (inheritance)

class Employees():
    def __init__(self):
        self.FirstName=""
        self.LastName =""
        self.Address =""
        
class DataScience(Employees):
    def __init__(self):
        self.Programming=""
    
class Marketing(Employees):
    def __init__(self):
        self.StoryTelling="" 
    
veribilimci = DataScience()
mar1 = Marketing()

##Fonksiyonel Programlama
# Yan etkisiz Fonksiyonlar (Pure Function)

#Örnek1: bağımsızlık

A = 9
def impure_sum(b): 
    return b+A
def pure_sum(a,b): # yan etkisiz 
    return a + b

impure_sum(6)
pure_sum(3,4)    


#Örnek2 Ölümcül yan etkiler
#OOP

class LineCounter:
    def __init__(self,filename):
        self.file = open(filename,"r")
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self,lines)
    
lc = LineCounter("deneme.txt")

print(lc.lines)
print(lc.count())
lc.read()
print(lc.lines)
print(lc.count())

#FP

def read(filename):
    with open(filename,"r") as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

ex_lines = read("deneme.txt")
lin_count = count(ex_lines)
lin_count


#İsimsiz fonksiyonlar (Anonymos Functions)

def old_sum(a,b):
    return a+b
old_sum(4,5)

new_sum = lambda a,b: a+b
new_sum(4,5)

sirasiz_liste = [("a",9),("b",8),("c",7),("d",6)]
sirasiz_liste
sorted(sirasiz_liste,key = lambda x:x[1])$#isimlendirme yapmadan ikinci indexi sıraladık

#Vektörel operasyonlar

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0,len(a))
for i in range(0,len(b)):
    print(i)
    ab.append(a[i]*b[i])
    
ab

import numpy as np

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
a*b

#map,filter ve reduce fonksiyonları

liste = [1,2,3,4,5]

for i in liste:
    print(i + 10)
    
list(map(lambda x: x*10,liste)) #Verilen bir nesnenin üzerinde fonksiyon çalıştırmaya yarar (isimsizdir)

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x %2 ==0,liste)) #Verilen bir nesnenin içinde koşulları arar. Yani değerleriyle bir işlem yapmadı sadece o değerleri getirdi

list(filter(lambda x: x %2 ==1,liste))

from functools import reduce

liste = [1,2,3,4]
reduce(lambda a,b: a+b,liste)

#Modül oluşturma

#Önce yeni HesapModulu adında pyton sayfası açıp bir fonksiyon yazdık.
#O fonksiyonu çağırmak için çesiştli yöntemler

import HesapModulu

HesapModulu.yeni_maas(1000)

import HesapModulu as hm
hm.yeni_maas(1000)
hm.yeni_maas

from HesapModulu import yeni_maas
yeni_maas(4000)

#Hatalar ve İstisnalar
#ZeroDivisionError hatası
a = 10
b = 0 

a/b

try:
    print(a/b)
    
except ZeroDivisionError:
    
    print("Payda da sıfır olmaz")

#tip hatası
    
a = 10 
b = "2"

a / b
try:
    print(a/b)
    
except TypeError:
    
    print("sayı ve string problemi")
