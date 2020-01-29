list(filter(lambda x: len(x) > 8, ["pazartesi","sali","carsamba","persembe","cuma"]))

a = [1,2,3]
list(map(lambda x: x*2, a))

liste = ["a",20,10,30,"b"]
list(filter(lambda x: type(x) == int, liste))

list(map(lambda x: x.upper(), ["Ali","Veli","isik"]))

list(filter(lambda x: x < 2, [1,2,3,4,5]))

list(map(lambda x: x*1, [2,7,4]))

from functools import reduce
reduce(lambda a,b: a/b, [8,4,2])

A = [[1,2],[3,4],[5,6]]
list(map(lambda x: x[0]*3, A))

from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))

fun = lambda x: x**2
fun(3)

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A, B]

for i in AB:
    if type(i[0]) == str:
        print(list(map(lambda x: x + " hi", i)))  
        
import numpy as np
a = np.array([1,1,1])
b = np.array([2])

a+b

A = [1,2,3,4,5]

if type(A) == ():
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))
    
list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50])))
