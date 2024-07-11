class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def grading (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        summ = 0
        count = 0
        for course in self.grades:
            if course in self.grades:
                summ += sum(self.grades[course])
                count += len(self.grades[course])
        if count == 0:
            return "нет оценок"
        return round(summ/count,1)

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._average_grade()} \n'
                f'Курсы в процессе обучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __eq__(self, other):
        if len(self.grades) != 0 and len(other.grades) != 0:
            return self._average_grade() == other._average_grade()
        else:
            return "нет оценок у одного из студентов"

    def __lt__(self, other):
        if len(self.grades) != 0 and len(other.grades) != 0:
            return self._average_grade() < other._average_grade()
        else:
            return  "нет оценок у одного из студентов"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade_lecturer(self):
        summ = 0
        count = 0
        for course in self.grades:
            if course in self.grades:
                summ += sum(self.grades[course])
                count += len(self.grades[course])
        if count == 0:
            return "нет оценок"
        return round(summ / count, 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average_grade_lecturer()}'

    def __eq__(self, other):
        if len(self.grades) != 0 and len(other.grades) != 0:
            return self._average_grade_lecturer() == other._average_grade_lecturer()
        else:
            return  "нет оценок у одного из лекторов"

    def __lt__(self, other):
        if len(self.grades) != 0 and len(other.grades) != 0:
            return self._average_grade_lecturer() < other._average_grade_lecturer()
        else:
            return  "нет оценок у одного из лекторов"


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
           if course in student.grades:
                student.grades[course] += [grade]
           else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def grades_course_students(list_student, course):
    summ = 0
    count = 0
    for student in list_student:
        if course in student.grades and isinstance(student,Student):
            summ += sum(student.grades[course])
            count += len(student.grades[course])
    if count == 0:
        return f'Нет оценок студентам по курсу {course}' if course in student.courses_in_progress else f'Нет такого курса в изучаемых'
    middle = round(summ / count, 1)
    return f'Средняя оценка по студентам в рамках {course}: {middle}'

def grades_course_lectures(list_lecturer, course):
    summ = 0
    count = 0
    for lecturer in list_lecturer:
        if course in lecturer.grades and isinstance(lecturer, Lecturer):
            summ += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
        else:
            'нет'
    if count == 0:
        return f'Нет оценок лекторам по курсу {course}' if course in lecturer.courses_attached else f'Нет такого курса в изучаемых'
    middle = round(summ/count,1)
    return f'Средняя оценка по лекторам в рамках {course}: {middle}'

student_1 = Student("Саня","Санин", "муж")
student_2 = Student("Сеня","Сенин", "муж")
lecturer_1 = Lecturer("Леха","Лехин")
lecturer_2 = Lecturer("Лена", "Ленина")
reviewer_1 = Reviewer("Петя", "Петров")
reviewer_2 = Reviewer("Павел", "Павлов")

student_1.add_finished_courses("Введение в программирование")
student_1.courses_in_progress += ["Python"]
student_1.courses_in_progress += ["Git"]
student_2.add_finished_courses("Введение в программирование")
student_2.courses_in_progress += ["Python"]
student_2.courses_in_progress += ["Git"]

lecturer_1.courses_attached += ["Git"]
lecturer_2.courses_attached += ["Python"]

reviewer_1.courses_attached += ["Git"]
reviewer_2.courses_attached += ["Python"]

reviewer_1.rate_hw(student_1, "Git", 10)
reviewer_1.rate_hw(student_2, "Git", 9)
reviewer_2.rate_hw(student_1, "Python", 7)
reviewer_2.rate_hw(student_2, "Python", 6)

student_1.grading(lecturer_1, "Git", 10)
student_1.grading(lecturer_2, "Python", 9)
student_2.grading(lecturer_1, "Git", 10)
student_2.grading(lecturer_2, "Python",8 )

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

print(student_1 == student_2)
print(student_1 < student_2)

print(lecturer_1 == lecturer_2)
print(lecturer_1 < lecturer_2)

print(grades_course_students([student_1,student_2], "Git"))
print(grades_course_lectures([lecturer_1,lecturer_2], "Python"))



