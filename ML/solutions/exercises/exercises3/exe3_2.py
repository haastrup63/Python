import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 

df = pd.read_csv('../winequality-red.csv', sep=";")
df['goodquality'] = [1 if x >= 6 else 0 for x in df['quality']]
df = df.drop('quality', axis=1)

X = df.drop('goodquality', axis=1)
X = X.to_numpy()
y = df['goodquality']
y = y.to_numpy()

gq_counts = df['goodquality'].value_counts() 
baseline = max(gq_counts) / (gq_counts[0] + gq_counts[1])

train_x, test_x, train_y, test_y = train_test_split(X,y, test_size=0.20, random_state=42)
model = DecisionTreeClassifier(max_depth=3).fit(train_x, train_y)
pred_y = model.predict(test_x)
accuracy = accuracy_score(test_y, pred_y)
print("Baseline: ", baseline)
print(accuracy)

plot_tree(model)
plt.show()