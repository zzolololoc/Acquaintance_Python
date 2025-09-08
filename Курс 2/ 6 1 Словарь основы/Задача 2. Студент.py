"""
Пользователь вводит фамилию, имя студента, город проживания, вуз, в котором он учится, и все его оценки.
Всё вводится в одну строку через пробел.
Напишите программу, которая по этой информации составит словарь и выведет его на экран.

Пример:

Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): Илья Иванов Москва МГУ 5 4 4 4 5

Результат:

Имя - Илья

Фамилия - Иванов

Город - Москва

Место учёбы - МГУ

Оценки - [5, 4, 4, 4, 5]
"""

info_student_input = input(
    "Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): "
)

info_student_list = info_student_input.split()

info_student_dict = dict()

def dict_info(info_student_dict, info_student_list):
    info_student_dict["Имя"] = info_student_list[0]
    info_student_dict["Фамилия"] = info_student_list[1]
    info_student_dict["Город"] = info_student_list[2]
    info_student_dict["Место учебы"] = info_student_list[3]
    info_student_dict["Оценки"] = info_student_list[4:]


dict_info(info_student_dict,info_student_list)

print(f"Имя - {info_student_dict["Имя"]}\n"
      f"Фамилия - {info_student_dict["Фамилия"]}\n"
      f"Город - {info_student_dict["Город"]}\n"
      f"Место учебы - {info_student_dict["Место учебы"]}\n"
      f"Оценки - {' '.join(info_student_dict["Оценки"])}\n")