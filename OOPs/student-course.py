class Student:
    number_of_student = 0

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        Student.add_student()

    def get_grades(self):
        return self.grades

    @classmethod
    def fun_number_of_people(cls):
        return cls.number_of_student

    @classmethod
    def add_student(cls):
        cls.number_of_student += 1

    # def just_try_super(self):
    #     print("Hope so it's work!")


# class Course(Student): JUST TRYING SUPER
class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []
        # super().just_try_super()

    def add_student(self, student):
        if (len(self.students) < self.max_students):
            self.students.append(student)
            return True
        return False

    def get_grades_average(self):
        sum = 0
        for student in self.students:
            sum += student.get_grades()
        return sum / len(self.students)


student_1 = Student("Akshit", 95)
student_2 = Student("Viral", 90)
student_3 = Student("Suru", 87)

course_science = Course("Computer Science", 2)
course_science.add_student(student_1)
course_science.add_student(student_2)
print(course_science.add_student(student_3))

print(course_science.students)

print(course_science.get_grades_average())
print(Student.fun_number_of_people())
