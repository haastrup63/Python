import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
np.set_printoptions(suppress=True)

df = pd.read_csv('../winequality-red.csv', sep=";")
df['good_quality'] = [1 if x >= 6 else 0 for x in df['quality']]
df = df.drop('quality', axis=1)

## Slightly better performance below 
attributes = ['fixed acidity', 'volatile acidity', 'citric acid', 'chlorides', 'residual sugar', 'density', 'pH', 'sulphates', 'good_quality']
print(list(df.columns))
print(attributes)
X = df[attributes]
X = X.to_numpy()
y = df['alcohol']
y = y.to_numpy()

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.20, random_state=42)

model = LinearRegression().fit(train_x, train_y)

pred_y = model.predict(test_x)

print(mean_squared_error(test_y, pred_y, squared=False))


print(model.coef_)