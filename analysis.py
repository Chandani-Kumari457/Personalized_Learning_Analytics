import pandas as pd

data = pd.read_csv("student_data.csv")

data["OverallScore"] = (
    0.4 * data["QuizScore"] +
    0.2 * data["Attendance"] +
    0.2 * data["CodingActivity"] +
    0.2 * data["TopicCompletion"]
)
def generate_recommendations(row):
    recommendations = []

    if row["QuizScore"] < 60:
        recommendations.append("Practice more quizzes and MCQs")

    if row["Attendance"] < 60:
        recommendations.append("Attend classes regularly")

    if row["CodingActivity"] < 60:
        recommendations.append("Solve coding problems daily")

    if row["TopicCompletion"] < 60:
        recommendations.append("Complete pending learning modules")

    if len(recommendations) == 0:
        return "Keep up the good work!"

    return " | ".join(recommendations)

data["Recommendations"] = data.apply(generate_recommendations, axis=1)

def find_weak_areas(row):
    weak = []

    if row["QuizScore"] < 60:
        weak.append("QuizScore")

    if row["Attendance"] < 60:
        weak.append("Attendance")

    if row["CodingActivity"] < 60:
        weak.append("CodingActivity")

    if row["TopicCompletion"] < 60:
        weak.append("TopicCompletion")

    if len(weak) == 0:
        return "No Weak Areas"

    return ", ".join(weak)
data["WeakAreas"] = data.apply(find_weak_areas, axis=1)

def performance_category(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    else:
        return "Needs Improvement"

data["Category"] = data["OverallScore"].apply(performance_category)
print(
    data[
        [
            "Student",
            "OverallScore",
            "Category",
            "WeakAreas",
            "Recommendations"
        ]
    ]
)