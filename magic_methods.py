class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector,
                      Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

        return res

    def average_rating(self):
        average = 0
        for course, rates in self.grades.items():
            for rate in rates:
                average += rate

        return average / len(self.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'

        return res

    def average_rating(self):
        average = 0
        for course, rates in self.grades.items():
            for rate in rates:
                average += rate

        return average / len(self.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_student = Student('Ruoy', 'Eman', 'man')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Boddy')
some_reviewer.courses_attached += ['Python', 'Git', 'Java', 'C']
some_lecturer = Lecturer('Some', 'Boddy')
some_lecturer.courses_attached += ['Python', 'Git', 'Java']

some_student.rate_lector(some_lecturer, 'Python', 10)
some_student.rate_lector(some_lecturer, 'Git', 7)
some_student.rate_lector(some_lecturer, 'Java', 8)

some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 4)

print(f'Reviewer:\n{some_reviewer}\n\n')
print(f'Lecturer:\n{some_lecturer}\n\n')
print(f'Student:\n{some_student}')
