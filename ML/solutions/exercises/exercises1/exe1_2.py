import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../winequality-red.csv", sep=";")
print("amount of rows: ",len(df))
print("attributes: ", list(df.columns))
print("basic statistics: \n",df.describe())

df['good_quality'] = [1 if x >= 6 else 0 for x in df['quality']]
df = df.drop('quality', axis=1)

sns.pairplot(df, hue='good_quality', height=0.7)
plt.show()
