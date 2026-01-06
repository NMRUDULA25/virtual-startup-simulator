def investor_bot(users, revenue, cash):
    if users > 500 and revenue > 1000:
        return "Investor: Your growth looks promising. I am interested in funding your startup."
    elif cash < 100000:
        return "Investor: Cash burn is high. Improve financial stability before seeking funding."
    else:
        return "Investor: The idea has potential, but I need to see stronger traction."


def mentor_bot(users, revenue, cash):
    advice = []
    if users < 300:
        advice.append("Focus on user acquisition and marketing strategy.")
    if revenue < users * 3:
        advice.append("Consider revising pricing or monetization strategy.")
    if cash < 200000:
        advice.append("Reduce unnecessary expenses and extend runway.")
    if not advice:
        advice.append("Your startup is on the right track. Keep scaling carefully.")
    return advice


def customer_bot(quality, marketing):
    if quality > 0.7:
        return "Customer: The product quality is excellent. I would recommend it to others."
    elif marketing > 0.6:
        return "Customer: I heard about this product through ads. It looks interesting."
    else:
        return "Customer: The product is okay, but it needs improvement."
