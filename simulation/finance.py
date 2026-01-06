def calculate_finance(users, revenue_per_user, cash):
    revenue = users * revenue_per_user
    expenses = users * 2
    cash = cash + revenue - expenses
    return revenue, cash
