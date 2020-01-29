#Matematiksel İşlemler
print(9+5)
print(3*4)

#Konsola yazı yazma
print('Hello')

#Verinin tipini öğrenme
print(type(9.2))

print('a'+ '-b')

#String Methodları - Len ()

a = 'Geleceği_Yazanlar' # Değişken atama yapma
print(len(a))

#Upper-Lower Metodu (Harflerin hepsini büyük veya küçük yapar)
print(a.upper())
print(a.lower())
print(a.isupper())
print(a.islower())

#Replace Metodu (Harflerin yerlerini değiştirir)

b = a.replace('e','a')

#Stip Metodu (Karakter(ekleme yapmazsan boşluk) en sağdan ve en solda Kırpma metodu)

c = ' Turhan_Can_Kargin '
c.strip()

d = '*Turhan*'
d.strip('*')

#Diğer Metodları öğrenmek

dir(a) #Uygulayabileceğimiz fonksiyonları gösterir

#Substringler

a[3]
a[0:3] # : ifadesi 0'dan 3'e kadar 3 yok demek

#Tip Dönüşümleri

birinci_sayi = input() #İnput kullanıcıdan bilgi alır
toplama_iki = input()

type(birinci_sayi)

int(birinci_sayi) + int(toplama_iki)

int(11.5)
float(12)
round(15.5)
type(str(15))

# bir fonksiyondan önce ? koymak onun kullanışını ve bilgilerini görmemize yarar. (?print)

#Örnek soru 
ifade = "Merhaba!"
ifade = ifade.lower()
ifade = ifade.replace("!","")
ifade
