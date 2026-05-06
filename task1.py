import pandas as pd
df= pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv",skiprows=4)
print(df.head())
print(df.columns)
df=df[['Country Name','2020']]
df=df.dropna()
import matplotlib.pyplot as plt
plt.hist(df['2020'],bins=10)
plt.title("Population Distribution (2020)")
plt.table("Population")
plt.table("Numaber of countreis")
plt.show()
top10=df.sort_values(by='2020',ascending=False).head(10)
top10.plot(x='Country Name',y='2020',kind='bar')
plt.title("Top 10 Countries by population(2020)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.show()
import seaborn as sns
sns.histplot(df['2020'],bins=10,kde=True)
plt.savefig("histogram.png")
plt.savefig("barchart.png")
plt.show()
