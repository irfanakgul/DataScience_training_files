import pandas as pd

df = pd.read_csv("iris.csv") #csv dosyamiza girmek icin kullanilir. bunu df ye atadik.

#print(df.Species.unique()) # kac tur Species var onu verir. Unique, Kisacasi: o sutunda hangi cesit urunler var

#df.info() # df dosyasinda kac kolon urun ortalama max min gibi degerler hakkinda bilgiler verir.

#setosa = df[df.Species == "Iris-setosa"] #Species sutunundaki tum "Iris-setosa"  olanlari suz ve  setosa adli degiskene atadik

#versicolor = df[df.Species == "Iris-versicolor"] #usttekinin aynisi :)

import matplotlib.pyplot as plt


df1 = df.drop(["Id"], axis=1)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label= "setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label= "versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color="blue", label= "virginica")
plt.legend()# x y cizgisi olusturur
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()