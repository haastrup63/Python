import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv('../sa_heart.csv')
famhist = pd.get_dummies(df['famhist'])
df = df.join(famhist)
df = df.drop('famhist', axis=1)

X = df.drop('chd', axis=1)
X = X.to_numpy()
y = df['chd']
y = y.to_numpy()

train_x, test_x, train_y, test_y = train_test_split(X,y, test_size=0.20, random_state=42)
tree_depths = range(1,20)
accuracies = []
for i in tree_depths:
    model = DecisionTreeClassifier(max_depth=i).fit(train_x, train_y)
    pred_y = model.predict(test_x)
    accuracies.append(np.mean(test_y == pred_y))
plt.plot(accuracies)
plt.show()