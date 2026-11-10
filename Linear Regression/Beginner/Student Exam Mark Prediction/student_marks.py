import pandas as pd

data = {
    "Study_Hours": [1,2,3,4,5,6,
                    7,8,9,10,11,12],
    "Exam_Marks":[22,28,35,42,48,55,
              62,68,75,82,87,94]
}
df = pd.DataFrame(data)
df.to_csv("student_marks.csv",index=False)