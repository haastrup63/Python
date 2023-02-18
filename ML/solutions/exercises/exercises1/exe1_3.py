import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../sa_heart.csv", sep=",")
print("amount of rows: ",len(df))
print("attributes: ", list(df.columns))
print("basic statistics: \n",df.describe())

sns.pairplot(df, hue='chd', height=0.7)
plt.show()

famhist = pd.get_dummies(df['famhist'])
df = df.join(famhist)
df = df.drop('famhist', axis=1)
