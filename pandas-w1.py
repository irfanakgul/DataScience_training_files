import pandas as pd
import numpy as np

dictionary = {
    "name":["ali","veli","kenan","hilal","ayse","evren"],
    "age":[15,16,17,33,45,66],
    "maas":[100,150,240,350,110,220]
        }

dataFrame1 = pd.DataFrame(dictionary) #sozlugu duzenler,
print(dataFrame1)
#head = dataFrame1.head(3) # ensustten 3 tane satiri gosterir.
#tail = dataFrame1.tail(3)# en sondan 3 satiri gosterir.
#colums = dataFrame1.columns #kolon basliklarini soyler
#info = dataFrame1.info() # sozluk hakkinda bilgiler verir kac kolon, boyut, kac veri vs.
#dtypes = dataFrame1.dtypes # veri tiplerini soyler
#descripe = dataFrame1.describe() # sayisal veriler hakkinda bize bilgiler verir, standasrsapma, max ,min, dagilim, ortalama vs,
#print(dataFrame1["age"]) #sadece age kolonunu yazdirir.

dataFrame1["yeni kolon"] = [-1,-2,-3,-4,-5,-6] #yeni kolon kadar ekler, satir kadar deger girilmesi gerekir.

#print(dataFrame1.loc[:, "age"]) # age kisminin tamamini yazdirir.
#print(dataFrame1.loc[:3, "name":"maas"]) # name den maasa kadar olan sutunlari alir ilk 4 satirini yazdirir,
#print(dataFrame1.loc[::-1,:]) #butun listeyi alttan uste yazmaya basladi.
#print(dataFrame1.loc[:,:"name"]) #sadece name sutununu yazdirir.
#print(dataFrame1.loc[:,"name"]) #sadece name sutununu yazdirir
#print(dataFrame1.iloc[:,2]) #2 nolu kolonu alir (iloc)


filtre1 = dataFrame1.maas > 200 #maasi 200 den buyuk olanlari True ve False olarak verir.
filtrelenmis_data = dataFrame1[filtre1] #maasi 200 den yuksek olan true ve false larin degereini yani maasini gosterir.
filtre2 = dataFrame1.age < 20
#print(dataFrame1[filtre1 & filtre2]) # maasi 200den buyuk ve yasi 20 den kucuk olanlari alir.


ortalama_maas = dataFrame1.maas.mean() # pandas maasin ortalamasini alir
ortalama_maas_numpy = np.mean(dataFrame1) # numpy ile maas ortalamasini aldik.
dataFrame1["maas_seviyesi"] = ["dusuk" if ortalama_maas > each else "yuksek" for each in dataFrame1.maas] # yeni kolon ekledik ve maasi ortalamanin ustunde olanlari yiksek aldinda olanlara dusuk yazisi ekledik.
dataFrame1.columns = [each.lower() for each in dataFrame1.columns] # kolon isimlerinin hepsini kucuk harf yapar,

dataFrame1.drop(["yeni kolon"], axis=1, inplace=True) #yeni kolon adli sutunu siler, axis =1 demek sutunu siler, axis = 0 satiri siler,

idx = 0
new_col = [7, 8, 9]  # can be a list, a Series, an array or a scalar
dataFrame1.insert(loc=idx, column='A', value=new_col) #belirledigimiz alana sutun eklemek

data1 = dataFrame1.head()
data2 = dataFrame1.tail()
data_concat = pd.concat([data1, data2], axis = 0) #satirlari alir ve alt alta koyar

print(data_concat)