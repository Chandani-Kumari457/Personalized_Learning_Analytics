import pandas as pd
import random

data = []

for i in range(1, 1001):

    quiz = random.randint(35, 100)
    attendance = random.randint(40, 100)
    coding = random.randint(30, 100)
    completion = random.randint(35, 100)

    final_exam = round(
        0.4 * quiz +
        0.2 * attendance +
        0.2 * coding +
        0.2 * completion +
        random.randint(-5, 5)
    )

    final_exam = max(0, min(100, final_exam))

    data.append([
        f"Student_{i}",
        quiz,
        attendance,
        coding,
        completion,
        final_exam
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Student",
        "QuizScore",
        "Attendance",
        "CodingActivity",
        "TopicCompletion",
        "FinalExamScore"
    ]
)

df.to_csv("student_data.csv", index=False)

print("500 student records generated successfully!")