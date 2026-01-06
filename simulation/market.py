import random

def market_condition():
    conditions = {
        "Boom": 1.2,
        "Normal": 1.0,
        "Recession": 0.8
    }
    condition = random.choice(list(conditions.keys()))
    return condition, conditions[condition]


def competitor_pressure():
    return random.uniform(0.7, 1.0)
