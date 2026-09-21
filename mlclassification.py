import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = pd.read_csv("customers.csv")

data = data.dropna(subset=["will_churn"])

columns = [
    "Age",
    "income",
    "number_of_logins",
    "purchase_count",
    "last_login_days"
]

for column in columns:
    data[column] = data[column].fillna(data[column].median())

data["subscription"] = data["subscription"].map({
    "Basic": 0,
    "Premium": 1
})

X = data[
    [
        "Age",
        "income",
        "number_of_logins",
        "purchase_count",
        "last_login_days",
        "subscription"
    ]
]

y = data["will_churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)