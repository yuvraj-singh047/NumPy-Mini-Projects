#Project #1
#Analysing Scores of Students

import numpy as np

from numpy import random

scores=np.random.randint(1,101,size=50)

print(f"Scores:\n{scores}")

grade_A=(scores>=90) #Array of Boolean
grade_B=(scores>=80) & (scores<90)
grade_C=(scores>=70) &(scores<80)
grade_D=(scores>=60) &(scores<70)
grade_F=(scores<60)
score_gradeA=scores[grade_A]

count_A=np.sum(grade_A)
count_B=np.sum(grade_B)
count_C=np.sum(grade_C)
count_D=np.sum(grade_D)
count_F=np.sum(grade_F)

print(f"No of Students with Grades:\nGrade-A: {count_A}\nGrade-B: {count_B}\nGrade-C: {count_C}\nGrade-D: {count_D}\nGrade-F: {count_F}")

print(f"\nScores of Grade-A Students: {score_gradeA}")