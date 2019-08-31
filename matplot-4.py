import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("iris.csv")
df1=df.drop(["Id"], axis=1)
df.plot(grid= True, alpha= 0.9, subplots=True)

setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]

plt.subplot(3,3,1) # 3 taneyi, 1 ekranda, sirayla goster
plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label="setosa")
plt.ylabel("setosa- petallengthcm")

plt.subplot(3, 3, 2) # 3 taneyi, 1 ekranda, sirayla goster
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="orange", label="versicolor")
plt.ylabel("versicolor-petallengthcm")

plt.subplot(3, 3, 3) # 3 taneyi, 1 ekranda, sirayla goster
plt.plot(virginica.Id, virginica.PetalLengthCm, color="green", label="virginica")
plt.ylabel("virginica-petallengthcm")
plt.show()