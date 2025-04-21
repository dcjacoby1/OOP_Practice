# How can a student be enrolled in a course?

# How do you assign a grade to a student for a course?


# How do you calculate a student's GPA?

# How do you list all students in a course?

# How do you find the average grade in a course?

# How can a student drop a course?

# How do you get a student's transcript?

# How can you get the top student by GPA?

# How do you check for students at risk of failing (GPA < 2.0)?

class Student:
    def __init__(self, name, school):
        self.name = name
        self.courses = {}
        if self not in school.students:
            school.students.append(self)

    def enroll(self, course):
        self.courses[course] = None
        course.add_student(self)
    
    def assign_grade(self, course, grade):
        if self.courses[course]:
            self.courses[course] = grade
        else:
            print("course does not exist")

    def drop_course(self, course):
        del self.courses[course]
        course.remove_student(self)

    def gpa(self):
        grades = [grade for grade in self.courses.values() if grade is not None]
        print(grades)
        average_grade = sum(grades)/len(grades)
        if average_grade >= 90:
            return 4.0
        elif average_grade >= 80:
            return 3.5
        elif average_grade >= 70:
            return 3.0
        elif average_grade >= 60:
            return 2.0
        else:
            return 0.0
        
    def get_transcript(self):
        print(f"transcript for {self.name}")
        for course, grade in self.courses.items():
            course_name = course.name
            if grade is not None:
                grade_value = grade
            else:
                grade_value = "In Progress"
            
            print(f"{course_name}: {grade_value}")
        print(f"gpa: {self.gpa()}")

            


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        if not student in self.students:
            self.students.append(student)
        else:
            print("student already added")
    
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def course_students(self):
        return self.students
    
    def average_grade(self):
        #course -> students in course -> for each student use dict to get the grade -> sum all the grades
        grades = [student.courses[self] for student in self.students if student.courses[self] is not None]
        return sum(grades)/len(grades)
    


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def expell_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def top_student(self):
        return max(self.students, lambda s: s.gpa(), default=None)
    
    def student_at_risk(self):
        return [student for student in self.students if student.gpa() < 2.0]












# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.courses = []

# class Course:
#     def __init__(self, course_name):
#         self.course_name = course_name
#         self.students = []

#     def enroll(self, student):
#         if not student in self.students:
#             self.students.append(student)
    
#     def enrolled_students(self):
#         return self.students

#     def drop_course(self, student):
#         if student in self.students:
#             self.remove(student)



# class Grade:
#     def __init__(self, student, course, grade):
#         self.student = student
#         self.course = course
#         self.grade = grade

#     def average_course_grade(self, course):
#         count = 0
#         grade_count = 0
#         if self.course == course:
#             grade_count += self.grade
#             count += 1
#         return grade_count / count


#     def gpa(self, student):
#         count = 0
#         grade_count = 0
#         if self.student == student:
#             grade_count += self.grade
#             count += 1
#         average_grade = grade_count / count
#         if average_grade >= 90:
#             return 4.0
#         elif average_grade >= 80:
#             return 3.5
#         elif average_grade >= 70:
#             return 3.0
#         elif average_grade >= 60:
#             return 2.0
#         else:
#             return 0.0
    

    
