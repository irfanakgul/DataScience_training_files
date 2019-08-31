import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")
setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]

#histogram cizimi

plt.hist(setosa.PetalWidthCm, bins = 50)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()



