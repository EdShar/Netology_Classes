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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
              f'{self.average_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'

        return res

    def average_rating(self):
        average = 0
        for course, rates in self.grades.items():
            for rate in rates:
                average += rate

        return average / len(self.grades)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_rating() < other.average_rating()


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

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() < other.average_rating()


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


def average_students(students, course):
    average_rates = 0
    average_len = 0

    for student in students:
        average_rates += sum(student.grades[course])
        average_len += len(student.grades[course])

    return average_rates / average_len

def average_lectors(lectors, course):
    average_rates = 0
    average_len = 0

    for lector in lectors:
        average_rates += sum(lector.grades[course])
        average_len += len(lector.grades[course])

    return average_rates / average_len


some_student = Student('Ruoy', 'Eman', 'man')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

new_student = Student('Alex', 'Parker', 'man')
new_student.courses_in_progress += ['Python', 'Git']

some_reviewer = Reviewer('Some', 'Boddy')
some_reviewer.courses_attached += ['Python', 'Git', 'Java', 'C']

new_reviewer = Reviewer('Perl', 'Broom')
new_reviewer.courses_attached += ['Python', 'Git', 'Java', 'C']

some_lecturer = Lecturer('Some', 'Boddy')
some_lecturer.courses_attached += ['Python', 'Git', 'Java']

new_lecturer = Lecturer('Grace', 'Dilly')
new_lecturer.courses_attached += ['Python', 'Git', 'Java']

some_student.rate_lector(some_lecturer, 'Python', 10)
some_student.rate_lector(some_lecturer, 'Git', 7)
some_student.rate_lector(some_lecturer, 'Java', 8)

new_student.rate_lector(new_lecturer, 'Python', 5)
new_student.rate_lector(new_lecturer, 'Git', 3)
new_student.rate_lector(new_lecturer, 'Java', 6)

some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 4)
new_reviewer.rate_hw(some_student, 'Python', 8)
new_reviewer.rate_hw(some_student, 'Git', 3)

some_reviewer.rate_hw(new_student, 'Python', 10)
some_reviewer.rate_hw(new_student, 'Git', 8)
new_reviewer.rate_hw(new_student, 'Python', 9)
new_reviewer.rate_hw(new_student, 'Git', 7)

current_course = 'Git'
print(average_students([some_student, new_student], current_course))
print(average_lectors([some_lecturer, new_lecturer], current_course))