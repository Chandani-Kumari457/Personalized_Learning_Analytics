import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load data
data = pd.read_csv("student_data.csv")

# Features
X = data[
    [
        "QuizScore",
        "Attendance",
        "CodingActivity",
        "TopicCompletion"
    ]
]

# Target
y = data["FinalExamScore"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = r2_score(y_test, y_pred)

print("Model Accuracy:", accuracy)