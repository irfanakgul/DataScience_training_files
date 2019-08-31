import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7])
y = x*2+5

plt.bar(x,y)
plt.title("bar plot")
plt.xlabel("x cubugu")
plt.ylabel("y cubugu")
plt.show()