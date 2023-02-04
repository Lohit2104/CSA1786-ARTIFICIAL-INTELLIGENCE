import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
data = pd.read_csv("customer_data.csv")

# Divide the data into features (X) and target 
X = data.drop('will_buy', axis=1)
y = data['will_buy']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict the target values for the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
