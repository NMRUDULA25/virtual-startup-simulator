import numpy as np
from sklearn.linear_model import LinearRegression

def predict_growth(months, users_history, revenue_history):
    # Convert data to numpy arrays
    X = np.array(months).reshape(-1, 1)
    y_users = np.array(users_history)
    y_revenue = np.array(revenue_history)

    # Train models
    user_model = LinearRegression()
    revenue_model = LinearRegression()

    user_model.fit(X, y_users)
    revenue_model.fit(X, y_revenue)

    # Predict next month
    next_month = np.array([[months[-1] + 1]])
    predicted_users = int(user_model.predict(next_month)[0])
    predicted_revenue = int(revenue_model.predict(next_month)[0])

    return predicted_users, predicted_revenue


def startup_success_score(users, revenue, cash):
    score = 0
    if users > 300:
        score += 40
    if revenue > 800:
        score += 30
    if cash > 200000:
        score += 30
    return min(score, 100)
