import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AI Learning Dashboard",
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: white;
}

div[data-testid="stMetric"]{
    background-color:#1E1E2F;
    padding:20px;
    border-radius:15px;
    border:2px solid #4CAF50;
    text-align:center;
}

div[data-testid="stMetric"] label{
    color:#FFFFFF !important;
    font-size:18px !important;
    font-weight:bold !important;
}

div[data-testid="stMetric"] div{
    color:#00FFAA !important;
    font-size:32px !important;
    font-weight:bold !important;
}

</style>

""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------
st.title("🎓 AI-Powered Learning Analytics Dashboard")
st.markdown("### 🚀 Real-time Student Performance Prediction System")

st.success("Platform is running successfully!")

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:

    st.title("🎓 AI Dashboard")

    st.info("Real-time Student Performance System")

    st.markdown("### 📌 Features")
    st.write("✔ Predict Final Score")
    st.write("✔ Risk Analysis")
    st.write("✔ Weak Areas Detection")
    st.write("✔ Personalized Study Plan")

    st.markdown("### 🧠 Model Info")
    st.write("Model: Linear Regression")
    st.write("Dataset: 1000 Students")

# ----------------------------
# LOAD DATA
# ----------------------------
data = pd.read_csv("student_data.csv")

# ----------------------------
# TRAIN MODEL
# ----------------------------
X = data[["QuizScore", "Attendance", "CodingActivity", "TopicCompletion"]]
y = data["FinalExamScore"]

model = LinearRegression()
model.fit(X, y)

# ----------------------------
# INPUT SECTION
# ----------------------------
st.header("🧑‍🎓 Student Input Panel")

col1, col2 = st.columns(2)

with col1:
    student_name = st.text_input("Student Name")
    quiz = st.number_input("Quiz Score", 0, 100,)
    coding = st.number_input("Coding Activity", 0, 100,)

with col2:
    attendance = st.number_input("Attendance", 0, 100,)
    completion = st.number_input("Topic Completion", 0, 100)

# ----------------------------
# PREDICTION BUTTON
# ----------------------------
if st.button("🚀 Analyze Performance"):
    
    st.write("BUTTON CLICKED SUCCESSFULLY")

    # Prediction
    predicted_score = model.predict([[quiz, attendance, coding, completion]])[0]



    st.header("📊 AI Result")

    st.success(f"🎯Predicted Score: {predicted_score:.2f}")
    col1, col2, col3 = st.columns(3)



    st.write("👤 Student:", student_name)

    st.subheader("📋 Student Report Card")

    report = pd.DataFrame({
    "Parameter": ["Quiz", "Attendance", "Coding", "Completion"],
    "Score": [quiz, attendance, coding, completion]
})

    st.table(report)

  
    # ----------------------------
    # RISK LEVEL
    # ----------------------------
    st.subheader("🎯 Student Category")

    if predicted_score < 50:
     category = "Weak Student"
    elif predicted_score < 80:
     category = "Average Student"
    else:
     category = "Excellent Student"

    st.write(category)
    st.session_state.history.append({
    "Student": student_name,
    "Predicted Score": round(predicted_score, 2),
    "Category": category
})
    st.subheader("🏅 Achievement Badge")

    if predicted_score >= 90:
     st.success("🌟 Star Performer")
    elif predicted_score >= 75:
     st.success("🥇 Excellent Learner")
    elif predicted_score >= 60:
     st.info("📚 Consistent Learner")
    else:
     st.warning("🚀 Rising Learner")
    # ----------------------------
    # PERSONALIZED PLAN
    # ----------------------------
    st.subheader("⏱ Study Plan")

    if predicted_score < 50:
        st.write("👉 Study 2–3 hours daily")
        st.write("👉 Focus on basics")
        st.write("👉 Revise previous topics")

    elif predicted_score < 80:
        st.write("👉 Practice coding daily")
        st.write("👉 Improve weak areas")
        st.write("👉 Solve mock tests")

    else:
        st.write("👉 Do advanced projects")
        st.write("👉 Participate in hackathons")

    st.subheader("📊 Coding Skill Level")

    if coding < 50:
     st.write("Beginner Level")
    elif coding < 80:
     st.write("Intermediate Level")
    else:
     st.write("Advanced Level")


    # ----------------------------
    # OVERALL SCORE
    # ----------------------------
    st.subheader("🏆 Performance Highlights")

    scores = {
    "Quiz": quiz,
    "Attendance": attendance,
    "Coding": coding,
    "Completion": completion
}

    best_area = max(scores, key=scores.get)
    weakest_area = min(scores, key=scores.get)

    st.success(f"Best Area: {best_area}")
    st.warning(f"Needs Most Improvement: {weakest_area}")

    st.subheader("📅 Attendance Analysis")

    if attendance >= 90:
     st.success("Excellent attendance record")
    elif attendance >= 75:
     st.info("Good attendance")
    else:
     st.warning("Attendance needs improvement")

    # ----------------------------
    # WEAK AREAS
    # ----------------------------
    st.subheader("⚠ Weak Areas")

    if quiz < 60:
        st.write("• Quiz Score weak")
    if attendance < 60:
        st.write("• Attendance weak")
    if coding < 60:
        st.write("• Coding weak")
    if completion < 60:
        st.write("• Topic Completion weak")

    # ----------------------------
    # GRAPH
    # ----------------------------
    st.subheader("📊 Performance Chart")

    chart_data = pd.DataFrame({
        "Score": [quiz, attendance, coding, completion]
    }, index=["Quiz", "Attendance", "Coding", "Completion"])

    st.bar_chart(chart_data)
    st.subheader("🥧 Performance Distribution")

    fig, ax = plt.subplots()

    ax.pie(
    [quiz, attendance, coding, completion],
    labels=["Quiz", "Attendance", "Coding", "Completion"],
    autopct="%1.1f%%"
)
    report_df = pd.DataFrame({
    "Student Name": [student_name],
    "Predicted Score": [round(predicted_score, 2)],

    
    "Category": [category]
})

    csv_report = report_df.to_csv(index=False)

    st.download_button(
    label="📄 Download Student Report",
    data=csv_report,
    file_name=f"{student_name}_report.csv",
    mime="text/csv"
)

    st.pyplot(fig)

    st.subheader("🌟 Motivation Corner")

    if predicted_score < 50:
     st.write("Every expert was once a beginner. Keep learning!")
    elif predicted_score < 80:
     st.write("You are progressing well. Consistency is the key.")
    else:
     st.write("Outstanding work! Keep aiming higher.")

     st.header("🕒 Student Analysis History")

if len(st.session_state.history) > 0:
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df)

# ----------------------------
# DATASET VIEW
# ----------------------------
st.header("📄 Training Dataset")
st.dataframe(data)

# ----------------------------
# DOWNLOAD
# ----------------------------
csv = data.to_csv(index=False)

st.download_button(
    
    label="📥 Download Dataset",
    data=csv,
    file_name="student_data.csv",
    mime="text/csv"
)