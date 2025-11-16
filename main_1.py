import streamlit as st
from prediction_helper import predict

# --------------------- Page Config ---------------------
st.set_page_config(
    page_title="Lauki Finance: Credit Risk Modelling",
    page_icon="📊",
    layout="wide"
)

# --------------------- Page Title -----------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #FFFFFF; font-size: 45px;'>
         Finance: Credit Risk Modelling
    </h1>
    <p style='text-align: center; color: #AAAAAA; font-size: 18px;'>
        Predict loan approval risk with machine learning-powered insights
    </p>
    <br>
    """,
    unsafe_allow_html=True
)

# --------------------- Input Section ---------------------
st.markdown("### 📝 Applicant Information")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('Age', 18, 100, 28)
with row1[1]:
    income = st.number_input('Annual Income (₹)', 0, 20000000, 1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount (₹)', 0, 30000000, 1200000)

loan_to_income_ratio = loan_amount / income if income > 0 else 0

with row2[0]:
    st.metric("Loan to Income Ratio", f"{loan_to_income_ratio:.2f}")
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (Months)', 0, 360, 36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Average DPD', 0, 200, 20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', 0, 100, 0)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', 0, 100, 0)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', 0, 25, 2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

st.markdown("---")

# --------------------- Prediction Button ---------------------
center = st.columns([4, 2, 4])
with center[1]:
    clicked = st.button("🔍 Calculate Risk", use_container_width=True)

# --------------------- Output Section ---------------------
if clicked:
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("## 📊 Risk Assessment Results")
    st.markdown("<br>", unsafe_allow_html=True)

    colA, colB, colC = st.columns(3)

    with colA:
        st.metric("Default Probability", f"{probability:.2%}")

    with colB:
        st.markdown(
            f"""
            <div style='background-color:#222; padding:20px; border-radius:15px; text-align:center;'>
                <h3 style='color:#FFFFFF;'>Credit Score</h3>
                <p style='color:#00FF8A; font-size:35px; font-weight:bold;'>{credit_score}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with colC:
        color = "#00FF8A" if rating == "Good" else "#FFA500" if rating == "Fair" else "#FF4B4B"
        st.markdown(
            f"""
            <div style='background-color:#222; padding:20px; border-radius:15px; text-align:center;'>
                <h3 style='color:#FFFFFF;'>Rating</h3>
                <p style='color:{color}; font-size:30px; font-weight:bold;'>{rating}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# --------------------- Footer ---------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:14px; color:#777;'>Built  by Ayush Pandey</p>",
    unsafe_allow_html=True
)
