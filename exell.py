import glob
import pandas as pd

all_data = pd.DataFrame()
for f in glob.glob("C:\\Users\\mrakg\\PycharmProjects\\newconda2\\class\\*.xlsx"):
    df = pd.read_excel(f,"SheetName")
    all_data = all_data.append(df,ignore_index=True)

