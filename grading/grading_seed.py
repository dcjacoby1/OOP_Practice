#!/usr/bin/env python3
"""
Grading System Seed File - Interactive debugging environment for grading.py
Run this file with: python grading_seed.py
"""

# Import the classes from grading.py
from grading import Student, Course, School
import ipdb

# Create a school instance
school = School("Python Academy")

# Create some sample courses
course1 = Course("Python Programming")
course2 = Course("Data Structures")
course3 = Course("Algorithms")
course4 = Course("Web Development")

# Create some sample students
student1 = Student("Alice Johnson", school)
student2 = Student("Bob Smith", school)
student3 = Student("Charlie Brown", school)

# Enroll students in courses
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)
student2.enroll(course3)
student3.enroll(course2)
student3.enroll(course4)

# Assign grades
student1.assign_grade(course1, 95)
student1.assign_grade(course2, 88)
student2.assign_grade(course1, 92)
student2.assign_grade(course3, 85)
student3.assign_grade(course2, 78)
student3.assign_grade(course4, 90)

# Print initial state
print("\n=== Initial School State ===")
print(f"School: {school.name}")
print(f"Total students: {len(school.students)}")
print(f"Total courses: {len(school.courses)}")

# Set debug point - code will pause here when you run 'python grading_seed.py'
print("\n=== Debugger Starting ===")
print("You can now interact with the grading system.")
print("Available objects: school, course1-4, student1-3")
print("Example commands:")
print("  p student1.courses  # Print student's courses and grades")
print("  p student1.gpa()  # Calculate student's GPA")
print("  p course1.average_grade()  # Calculate course average")
print("  p school.top_student()  # Find top student by GPA")
print("  p school.student_at_risk()  # Find students at risk")
print("  c  # Continue execution")
print("  q  # Quit debugger")
ipdb.set_trace()

# After the debugger, you can continue with more operations
print("\n=== Debugger Session Ended ===")
print("Continuing with example operations...")

# Demonstrate course dropping
student1.drop_course(course2)
print(f"\n{student1.name} dropped {course2.name}")

# Demonstrate student expulsion
school.expell_student(student3)
print(f"\n{student3.name} was expelled from {school.name}")

# Print final state
print("\n=== Final School State ===")
print(f"School: {school.name}")
print(f"Total students: {len(school.students)}")

# Show student information
print("\n=== Student Information ===")
for student in school.students:
    print(f"\nStudent: {student.name}")
    print("Courses and Grades:")
    for course, grade in student.courses.items():
        grade_str = str(grade) if grade is not None else "In Progress"
        print(f"  - {course.name}: {grade_str}")
    print(f"GPA: {student.gpa()}")

# Show course information
print("\n=== Course Information ===")
for course in [course1, course2, course3, course4]:
    print(f"\nCourse: {course.name}")
    print(f"Students: {[student.name for student in course.students]}")
    print(f"Average Grade: {course.average_grade()}")

# Show top student
top_student = school.top_student()
if top_student:
    print(f"\nTop Student: {top_student.name} with GPA {top_student.gpa()}")
else:
    print("\nNo students found")

# Show students at risk
at_risk = school.student_at_risk()
if at_risk:
    print("\nStudents at Risk:")
    for student in at_risk:
        print(f"  - {student.name} with GPA {student.gpa()}")
else:
    print("\nNo students at risk")

print("\n=== Grading Seed Complete ===") 