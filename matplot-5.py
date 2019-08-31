import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel("quiz1-1.xlsx", sheet_name=None, ignore_index=True)
cdf = pd.concat(df.values(),sort=False)
cdf.replace("girmedi",np.nan,inplace=True)

