import streamlit as st
from simulation.growth import calculate_user_growth
from simulation.finance import calculate_finance
from simulation.market import market_condition, competitor_pressure
from ai.advisor import ai_advice
from ai.chatbots import investor_bot, mentor_bot, customer_bot
from ai.ml_predictor import predict_growth, startup_success_score


st.title("Virtual Startup Simulator")

startup = st.text_input("Startup Name")
quality = st.slider("Product Quality", 0.0, 1.0, 0.5)
marketing = st.slider("Marketing Effort", 0.0, 1.0, 0.5)
cash = st.number_input("Initial Cash (₹)", value=500000)
months = st.slider("Months", 1, 12, 6)
users_history = []
revenue_history = []
month_list = []


if st.button("Run Simulation"):
    users = 100
    revenue_per_user = 2

    st.subheader("📊 Simulation Results")

    for month in range(1, months + 1):
        condition, market_factor = market_condition()
        competitor_factor = competitor_pressure()

        users = calculate_user_growth(
            users, quality, marketing, market_factor, competitor_factor
        )

        revenue, cash = calculate_finance(users, revenue_per_user, cash)
        users_history.append(users)
        revenue_history.append(revenue)
        month_list.append(month)


        st.write(
            f"Month {month} | Market: {condition} | "
            f"Users: {users} | Revenue: ₹{revenue} | Cash: ₹{cash}"
        )

    # Final values after simulation
    final_users = users
    final_revenue = revenue
    final_cash = cash

    # 🤖 AI Decision Advisor
    st.subheader("🤖 AI Decision Advisor")
    advice = ai_advice(final_users, final_revenue, final_cash)
    for tip in advice:
        st.write("•", tip)

    # 💬 AI Chatbots
    st.subheader("💬 AI Chatbots Feedback")

    # Investor Bot
    st.markdown("### 🤝 Investor Bot")
    st.write(investor_bot(final_users, final_revenue, final_cash))

    # Mentor Bot
    st.markdown("### 🧠 Mentor Bot")
    mentor_feedback = mentor_bot(final_users, final_revenue, final_cash)
    for tip in mentor_feedback:
        st.write("•", tip)

    # Customer Bot
    st.markdown("### 🧑 Customer Bot")
    st.write(customer_bot(quality, marketing))
    st.subheader("📈 Machine Learning Predictions")
    pred_users, pred_revenue = predict_growth(month_list, users_history, revenue_history)
    st.write(f"🔮 Predicted Users (Next Month): {pred_users}")
    st.write(f"🔮 Predicted Revenue (Next Month): ₹{pred_revenue}")
    score = startup_success_score(final_users, final_revenue, final_cash)
    st.write(f"🏆 Startup Success Score: {score}/100")


