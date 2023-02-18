import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("../../Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv")
df['date'] = pd.to_datetime(df['Date'])
df['time'] = pd.to_datetime(df['Time'])

df_vehicletheft = df[df['Category'] == 'VEHICLE THEFT']
df_vehicletheft = df_vehicletheft[df_vehicletheft['date'].dt.year >= 2012]
df_vehicletheft_sampled = df_vehicletheft.sample(15000)

df_fraud = df[df['Category'] == 'FRAUD']
df_fraud = df_fraud[df_fraud['date'].dt.year >= 2012] 
df_fraud_sampled = df_fraud.sample(15000)

df_focus_crimes = pd.concat([df_vehicletheft_sampled, df_fraud_sampled])

pd_districts_encoded = pd.get_dummies(df_focus_crimes['PdDistrict'])
df_focus_crimes = df_focus_crimes.join(pd_districts_encoded)

df_focus_crimes['month'] = [x.month for x in df_focus_crimes['date']]
df_focus_crimes['hour'] = [x.hour for x in df_focus_crimes['time']]
df_focus_crimes['day_of_week'] = [x.dayofweek for x in df_focus_crimes['date']]

pd_districts = list(df.PdDistrict.unique()[:-1])
crime_features = ['day_of_week', 'hour', 'month'] + pd_districts

X_df = df_focus_crimes[crime_features]
X = X_df.to_numpy()
y_df = df_focus_crimes['Category']
y = y_df.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=42)

accuracies = []
for i in range(1,20):
    model = DecisionTreeClassifier(max_depth=i).fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracies.append(np.mean(y_pred == y_test))

print(accuracies)
plt.plot(accuracies)
plt.show()