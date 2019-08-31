import pandas as pd

df=pd.read_csv("iris.csv")
#pandastan dolayi direk dataframe oldu
print(df.columns)
#eger read_csv dersem calistigi yerde arar.
print(df.Species.unique)
#unique olanlari verir
print(df.info())
setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
print(setosa.describe())
print(versicolor.describe())
#atilan dosyalar birlestirilecek. tek dosya olacak irfan akgulu seceyim sonuclarini getirsin
import matplotlib.pyplot as plt
#uc boyutlu goruntuelemelerde pyplot isimize yaramayacak baska paketlere
#gececegiz. pyplot en genel kullanani.
df1=df.drop(["Id"], axis=1)
#ataframeden o kolon cikarilacak cunku id kolonu isime yaramayacak
setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]
plt.plot(setosa.Id,setosa.PetalLengthCm, color="red", label="setosa")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label="virginica")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor")
plt.legend()
#legend x ve y yi olusturur
plt.xlabel("Id")
#x label'i
plt.ylabel("PetalLengthCm")
#show demezseniz gostermez.
plt.show()