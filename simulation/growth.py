import random

def calculate_user_growth(current_users, quality, marketing, market_factor, competitor_factor):
    base_growth = (quality * 0.5) + (marketing * 0.5)
    growth = current_users * base_growth * market_factor * competitor_factor
    noise = random.randint(5, 25)
    return int(current_users + growth + noise)
