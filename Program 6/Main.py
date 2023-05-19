# Author: Jacob Sprouse
# Assignment Title: Program 6
# Assignment Description: Grade calculator
# Due Date: 05/12/2023
# Date Created: 04/26/2023
# Date Last Modified: 05/09/2023

# maximum possible points
HOMEWORK_MAX_GRADE = 800.0
QUIZZES_MAX_GRADE = 400.0
MIDTERM_MAX_GRADE = 150.0
FINAL_MAX_GRADE   = 200.0

# input and input validator
category = input()
invalid_input = False

# sorts the grading scale by student status
if category == 'UG':
    homework_grade_scale = .2
    quizzes_grade_scale = .2
    midterm_grade_scale = .3
    final_exam_grade_scale = .3
elif category == 'G':
    homework_grade_scale = .15
    quizzes_grade_scale = .05
    midterm_grade_scale = .35
    final_exam_grade_scale = .45
elif category == 'DL':
    homework_grade_scale = .05
    quizzes_grade_scale = .05
    midterm_grade_scale = .4
    final_exam_grade_scale = .5

# checks for valid student status
if (category != 'UG') and (category != 'G') and (category != 'DL'):
    invalid_input = True
else:
    # score inputs
    homework_grade = float(input())
    quiz_grade     = float(input())
    midterm_grade  = float(input())
    final_grade    = float(input())

    # Calculate course average
    homework_avg = (homework_grade / HOMEWORK_MAX_GRADE) * 100
    quiz_avg = (quiz_grade / QUIZZES_MAX_GRADE) * 100
    midterm_avg = (midterm_grade / MIDTERM_MAX_GRADE) * 100
    final_exam_avg = (final_grade / FINAL_MAX_GRADE) * 100

    # correct excessive grade
    if homework_avg > 100:
        homework_avg = 100
    if quiz_avg > 100:
        quiz_avg = 100
    if midterm_avg > 100:
        midterm_avg = 100
    if final_exam_avg > 100:
        final_exam_avg = 100

    # calculates students final average
    course_average = 0
    course_average = (homework_avg * homework_grade_scale) + (quiz_avg * quizzes_grade_scale) \
              + (midterm_avg * midterm_grade_scale) + (final_exam_avg * final_exam_grade_scale)

    # final grade  scale
    if course_average >= 90:
        course_grade = 'A'
    elif course_average >= 80.0:
        course_grade = 'B'
    elif course_average >= 70.0:
        course_grade = 'C'
    elif course_average >= 60.0:
        course_grade = 'D'
    else:
        course_grade = 'F'

# Output
if invalid_input:
    print("Error: student status must be UG, G or DL")
else:
    print(f"Homework: {homework_avg:2.1f}%")
    print(f"Quizzes: {quiz_avg:2.1f}%")
    print(f"Midterm: {midterm_avg:2.1f}%")
    print(f"Final Exam: {final_exam_avg:2.1f}%")
    print(f"{category} average: {course_average:2.1f}%")
    print(f"Course grade: {course_grade}")
