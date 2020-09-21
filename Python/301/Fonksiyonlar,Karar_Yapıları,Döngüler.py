#Fonksiyonlara giriş ve fonksiyon okuzyazarlığı
print() #Ekrana yazı yazdıran fonksiyon
print("a","b", sep="-")

len("a") #Uzunluk fonksiyonu

#Matematiksel İşlemler

4*4
4/4
5-1
6+3
3**2
3**3

#Fonsiyon Nasıl Yazılır?

def kare_al(x):
   print(x**2)
    
kare_al(3) #kare_al artık fonksiyondur

#Bilgi notuyla çıktı üretmek

def kare_al(x):
   print("Girilen Sayının Karesi:" + str(x**2)) #Sitringle string kullanılır diye str( ) yaptık
  
kare_al(3)    
   
def kare_al(x):
   print("Girilen Sayı "+str(x)+ 
         ", Karesi:" + str(x**2))
   
kare_al(3)       

#İki Argümanlı fonksiyon tanımlama

def carpma_yap(x,y):
    print("Birinci Sayı:" + str(x) + " İkinci Sayı: " + str(y) + " Çarpım: " + str(x*y))

carpma_yap(3,5)    

#Ön Tanımlı Argümanlar

def carpma_yap(x,y=1):
    print(x*y)
    
carpma_yap(3) 
carpma_yap(3,4) # y'ye başka sayı atanabilir bu şekilde

#Argümanların sıralaması

def carpma_yap(x,y=1):
    print(x*y)
    
carpma_yap(y=2,x=5)# Fonksiyon içindeki argümanları biliyorsak böyle sıra önemi olmadan yazabiliriz. 


#Ne zaman fonksiyon yazılır?

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)
    
direk_hesap(30,40,50)   

#Tekrar tekrar kodu yazmak yerine fonksiyon tanımlayıp ileride tekrar kullanabliriz.

#Çıktıyı Girdi olarak kullanmak

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)
cikti = direk_hesap(30,40,50)
cikti #Çıktıyı alamıyoruz

def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj
cikti = direk_hesap(25,40,70)
cikti# return kullanırsak çıktıyı girdi olarak kullanabilriz

#Local ve Global Değişkenler

x = 10
y = 20 # x ve y Global Değişkenlerdir

def carpma_yap(x,y):
    return x*y

carpma_yap(2,3) #Buradaki x ve ya local değişkendir

#Local etki alanından gloval etki alanını değiştirmek

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
    
eleman_ekle(1)
x
eleman_ekle("ali")
x

##Karar Kontrol Yapıları

# True False Sorgulamaları

sinir = 500

sinir == 4000 # Doğruluk cevabı verir (== ifadesi denk mi diye sorar)
sinir == 500    

5 == 4
5 == 5

# İF ifadesi
toplam = 50000
gelir = 50000
gelir < toplam
if gelir < toplam:
    print("Gelir toplamdan küçük")
    print(gelir*2)
    
    
#Else yapısı
if gelir < toplam:
    print("Gelir toplamdan küçük")
    
else:
    print("Gelir toplamdan büyük")


if gelir == toplam:
    print("Gelir toplama eşit")
    
else:
    print("Gelir toplamdan büyük")
    
# elif

toplam = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > toplam:
    print("Tebrikler")
    
elif gelir1 < toplam:
    print("Uyarı!")
 
else:
    print("Takibe Devam")
    
    
if gelir2 > toplam:
    print("Tebrikler")
    
elif gelir2 < toplam:
    print("Uyarı!")
 
else:
    print("Takibe Devam")
    
if gelir3 > toplam:
    print("Tebrikler")
    
elif gelir3 < toplam:
    print("Uyarı!")
 
else:
    print("Takibe Devam")
    
#Mini Uygulama
sinir = 50000
magaza_adi = input("Magaza adı nedir?")
gelir = int(input("Geliriniz nedir?"))

if gelir > sinir:
    print("Tebrikler " + magaza_adi + " Promosyon Kazandınız")

elif gelir < sinir:
    print("Uyarı " + str(gelir) + " Lira geliriniz var ")
else:
    print("Devam")

#Döngüler - For
    
ögrenci = ["ali","veli","isik","berk"]
ögrenci[0]

for i in ögrenci:
    print(i)
    
maas = [1000,2000,3000,4000,5000]

for i in maas:
    print(int(i/10))
    
#Mini Uygulama

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100 + x)
def maas_alt(x):
    print(x*20/100 + x)

for i in maaslar:
    if i >= 3000:
        maas_ust(i)
        
    else:
        maas_alt(i)

#Break & Continue
maaslar = [8000,5000,2000,1000,3000,7000,1000]
maaslar.sort() # Sıralamak için
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break # Döngüyü keser
    print(i)

for i in maaslar:
    if i == 3000:
        continue # değer atlama
    print(i)
    
    
#While

sayi = 1
while sayi < 10:
    sayi += 1 # Üzerine 1 ekle, atama yap
    print(sayi)
