def ai_advice(users, revenue, cash):
    advice = []

    if users < 200:
        advice.append("User growth is low. Consider increasing marketing efforts.")

    if revenue < 500:
        advice.append("Revenue is limited. Improve pricing or value proposition.")

    if cash < 100000:
        advice.append("Warning: Cash reserves are running low. Reduce expenses or seek investment.")

    if not advice:
        advice.append("Your startup is performing well. Continue current strategy.")

    return advice
