#1-Veri Yapıları

#a.Listeler = ([],list())

notlar = [90,80,70,50]

type(notlar)

liste = ['a',19.3,90] #Farklı veri tipleri barındırabilir

liste2 = [liste,notlar] # Liste içinde Liste tanımlamak, listeleri birleştirme
len(liste2)
liste3 = [9,10,liste2]
len(liste3)

type(liste3) #Geonel Tipi sorgulama

#ayrı ayrı tip sorgulama
type(liste[0])
type(liste[1])
type(liste[2])

#Liste silmek
liste4 = [1,2,3,4]
del liste4

#Liste elemanına erişme yöntemleri

Sayılar = [10,20,30,40,50]

Sayılar[0]
Sayılar[1]
Sayılar[2]
Sayılar[5]# aralık dışında hatası verir

Sayılar[0:2]
Sayılar[:2]
Sayılar[2:]

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste
yeni_liste[2]

#Liste içindeki listeye erişme
yeni_liste[2][1]

#Listelere eleman ekleme, değiştirme ve silme

isimler = ["Ali","Veli","Berkcan","Ayse"]

isimler[1] = "velinin_babasi"

isimler

isimler[:3] = "alinin_babasi","velinin_babası","berkcanin_babasi"
isimler

isimler = isimler + ["Kemal"]
isimler

del isimler[2]
isimler
#Fonksiyonlarla eleman ekleme,çıkarma
isimler2 = ["ali","veli","isik"]
dir(isimler2) #metod bulma 

isimler2.append("berkan")
isimler2

isimler2.remove("isik")
isimler2

#indexe göre eleman ekleme ve silme

isimler2

isimler2.insert(0,"ayse")
isimler2

isimler2.insert(3,"mehmet")
isimler2

isimler2.insert(len(isimler2),"beren")
isimler2

isimler2.pop(4)
isimler2


#Diğer liste metodları

List = [1,2,3,4,5,6,7,8,1,2,4,5,6,9]

List.count(1) #Frekans (kaç tane var)
List_Backup = List.copy() # yedekleme yapar
List.extend([10,20,30]) #Listeyi genişletir
List
List.index(5) # Kaçıncı sütünda onu söyler
List.reverse() #Tersine çevirir
List 
List.sort() #Sıralama yapar (küçükten büyüge)
List
List.clear() #Listeyi temizler(tüm elemanları siler)
List


#b.Tuple

#Tuple oluşturma = tuple()

t = ("ali","veli",1,2,3,2,[1,2,3,4])
t1 = ("eleman",) #Tek eleamlılarda sona virgül koyarsak tuple larak algılanır
type(t1)

#Tuple eleman işlemleri

t[1]
t[:3]

t[2] = 99 #'tuple' object does not support item assignment

#Liste ve tuple farkı tuple'da değişiklik yapmayız böylece eğer değişiklik isemiyorsak tuple kullanmak daha mantıklı.


#c- Sözlükler

#Sözlük oluşturma

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}
sozluk

len(sozluk)


sozluk2 = {"REG" : 1,
          "LOJ" : 2,
          "CART": 3}
sozluk2

sozluk3 = {"REG" : ["Regresyon Modeli",1],
          "LOJ" : ["Lojistik Regresyon",2],
          "CART": ["Classification and Reg",3]}
sozluk3

#Sözcüklerde eleman seçme işlemleri

sozluk3[0] #Sözlükler sırasızdır o yüzden index algılamaz

sozluk3["REG"] #Key Word'ü yazmamız gerekli
#Sözlük içinde sözlük
sozluk4 ={"REG" : {"Regresyon Modeli": 1,
           "Lojistik Regresyon": 2,
           "Classification and Reg":3}
sozluk4["REG"]["Regresyon Modeli"]

#Sözülük Eleman ekleme ve değiştirme

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk
sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk
 
sozluk[1] = "yapay sinir ağları"
sozluk

l = [1]

sozluk[l] = "yeni bir şey" #unhashable type: 'list' hatası alınır çünkü key oluştururken sabit veri yapısı alır

t = ("tuple") # Tuple sabit veri yapısı olduğu için key olarak kullanılabilir
sozluk[t] = "yeni bir şey"
sozluk

#d- SETLER
#Sırasız,değerler tekrar edemez,değiştirilebilir ( Kümelere benzer)

l = [1,"a","ali",123]
s = set(l)
s

t = ("a","ali")
s = set(t)
s

ali = "ata_bak_ve_atı_sür"
type(ali)
s = set (ali)
s

l = ["ali","lutfen","ata","bak","ve","atı","sur","ali","at","ali","sur"]
s=set(l)
s
len(s)

s[0] #sette sıra yok hata alır

#setlerde eleman eklema ve çıkarma

l = ["gelecegi","yazanlar"]
s=set(l)
s

dir(s)

s.add("ile")
s

s.add("ile") #tekrar olmadığı için bir daha eklemez
s.remove("ile")
s


#Setlerde Fark İşlemleri: difference ve symmetric difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) #Set1de olup set2de olmayan
set2.difference(set1) #Set2de olup set1de olmayan

set1.symmetric_difference(set2) #ortak olmayan elemanlar
set2-set1#Set2de olup set1de olmayan

#Setlerde Kesişim ve Birleşim İşlemleri: intersection ve union

set1.intersection(set2) #kesişim
set1&set2#kesişim

set1.union(set2) #birleşim

set1.intersection_update(set2) #set1'e kesişimi atar
set1
set2

#Setlerde sorgulama işlemleri
set3 = set([7,8,9])
set4 = set([5,6,7,8,9,10])

set3.isdisjoint(set4) # Kesişim boş kümemi
set3.issubset(set4)# set3 set4'ün altkümesi mi
set4.issuperset(set3) #set3 set4'ü kapsar mı
