sozluk = {"reg" : "regresyon modeli",
"loj" : "lojistik regresyon",
"cart" : "classification and regression trees"}

sozluk["gbm"] = "gradient boosting machines"
sozluk

liste = ["A","B","C"]
liste[0] = "D"
liste.insert(0, "D")
liste
liste.append("D")
liste

set1 = set([5,7,9])
set2 = set([5,6,7])
set2.difference(set1)

liste = ["a","b","c"]
liste.extend(liste)
liste

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

sozluk = {"REG" : {"RMSE": 10,
"MSE": 11,
"SSE": 12},
 
"LOJ" : {"RMSE": 111,
"MSE": 2222,
"SSE": 333},
 
"CART" : {"RMSE": 99,
"MSE": 00,
"SSE": 66}}

sozluk["CART"]["SSE"]

t = ("a",10,"b")
t[0] = 1

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.difference(set2)

liste = [10,20,30,40]
liste.pop(1)
liste

liste = [1,1,2,3,4,5,1,2,1]
liste.count(1)