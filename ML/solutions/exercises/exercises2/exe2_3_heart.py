import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('../sa_heart.csv', sep=",")
famhist = pd.get_dummies(df['famhist'])
df = df.join(famhist)
df = df.drop('famhist', axis=1)

# Cant be improved
attributes = ['sbp', 'tobacco', 'ldl', 'adiposity', 'typea', 'obesity', 'alcohol', 'chd', 'Absent', 'Present']
X = df[attributes]
y = df['age']
y = y.to_numpy()

train_x, test_x, train_y, test_y = train_test_split(X,y, test_size=0.20, random_state=42)

model = LinearRegression().fit(train_x, train_y)

pred_y = model.predict(test_x)

print(mean_squared_error(test_y, pred_y, squared=False))
print(model.coef_)
print(df.columns)