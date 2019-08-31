import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")
setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]
plt.scatter(setosa.Id,setosa.PetalLengthCm, color="red", label="setosa")
plt.scatter(virginica.Id,virginica.PetalLengthCm,color="blue",label="virginica")
plt.scatter(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor")
plt.legend()
#legend x ve y yi olusturur
plt.xlabel("PetalLengthCm")
#x label'i
plt.ylabel("PetalLWidthCm")
#show demezseniz gostermez.
plt.title("scatter plot-2")
plt.show()

