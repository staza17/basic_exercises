# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

students_number = {}

for student in students:
    number = students.count(student)
    students_number[student['first_name']] = number
for key, value in students_number.items():
    print(f'{key}: {value}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def popular(names_dict):
    largest = 0
    popular_name = ''
    for key, value in names_dict.items():
        if largest < value:
            largest = value
            popular_name = key
    return popular_name

students_number = {}
for student in students:
    number = students.count(student)
    students_number[student['first_name']] = number

print(f'Самое частое имя среди учеников: {popular(students_number)}')



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for s_class in school_students:
    students_number = {}
    for student in s_class:
        number = s_class.count(student)
        students_number[student['first_name']] = number
    print(f'Самое частое имя в классе {school_students.index(s_class) + 1}: {popular(students_number)}')



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for s_class in school:
    girls = 0
    boys = 0
    for student in s_class['students']:
        for name in is_male:
            if name == student['first_name']:
                if is_male[name]:
                    boys += 1
                else:
                    girls += 1
    print(f'Класс {s_class['class']}: девочки {girls}, мальчики {boys}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

girls_largest_count = 0
boys_largest_count = 0
girls_class = ''
boys_class = ''

for s_class in school:
    girls = 0
    boys = 0
    for student in s_class['students']:
        for name in is_male:
            if name == student['first_name']:
                if is_male[name]:
                    boys += 1
                else:
                    girls += 1
    if girls_largest_count < girls:
        girls_largest_count = girls
        girls_class = s_class['class']
    if boys_largest_count < boys:
        boys_largest_count = boys
        boys_class = s_class['class']
print(f'Больше всего мальчиков в классе {boys_class}')
print(f'Больше всего девочек в классе {girls_class}')


