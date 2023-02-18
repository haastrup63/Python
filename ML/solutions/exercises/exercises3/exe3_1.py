import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score

df = pd.read_csv('../sa_heart.csv')
famhist = pd.get_dummies(df['famhist'])
df = df.join(famhist)
df = df.drop('famhist', axis=1)

X = df.drop('chd', axis=1)
X = X.to_numpy()
y = df['chd']
y = y.to_numpy()

chd_counts = df['chd'].value_counts() 
baseline = max(chd_counts) / (chd_counts[0] + chd_counts[1])

train_x, test_x, train_y, test_y = train_test_split(X,y, test_size=0.20, random_state=42)
model = LogisticRegression().fit(train_x, train_y)
pred_y = model.predict(test_x)
print("Baseline: ", baseline)
accuracy = accuracy_score(test_y, pred_y)
print(accuracy)