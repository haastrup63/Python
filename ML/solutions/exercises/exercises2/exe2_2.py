import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt 

df = pd.read_csv('../sa_heart.csv', sep=",")
famhist = pd.get_dummies(df['famhist'])
df = df.join(famhist)
df = df.drop('famhist', axis=1)

X = df.drop('age',axis=1)
X = X.to_numpy()
y = df['age']
y = y.to_numpy()

train_x, test_x, train_y, test_y = train_test_split(X,y, test_size=0.20, random_state=42)

model = LinearRegression().fit(train_x, train_y)

pred_y = model.predict(test_x)

print(mean_squared_error(test_y, pred_y, squared=False))

plt.scatter(pred_y, test_y)
plt.xlabel("Predicted Age")
plt.ylabel("True Age")
min = min([pred_y.min(), test_y.min()])
max = max([pred_y.max(), test_y.max()])
plt.axline((min, min), (max,max), color='black')
plt.show()