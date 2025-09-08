"""
Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, а также его текущий статус, в котором указано, отдыхает он, тренируется или путешествует:

players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}

Напишите программу, которая выводит на экран следующие данные в разных строках:

Все члены команды А, которые отдыхают.
Все члены команды B, которые тренируются.
Все члены команды C, которые путешествуют.

"""

import json

players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}


sorted_dict = {
    "a-Rest": [],
    "b-Training": [],
    "c-Travel": []
}



for key,values in players_dict.items():
    team = values.get("team")
    status = values.get("status")
    if team == "A" and status == "Rest":
        sorted_dict["a-Rest"].append({"name":values.get("name"), "status":values.get("status")})
    elif team == "B" and status == "Training":
        sorted_dict["b-Training"].append({"name": values.get("name"), "status": values.get("status")})
    elif team == "C" and status == "Travel":
        sorted_dict["c-Travel"].append({"name": values.get("name"), "status": values.get("status")})

print(json.dumps(sorted_dict, ensure_ascii=False, indent=4))











#Способ из 1 словаря с командами
# sorted_dict = {
#     "a-Rest": [],
#     "b-Training": [],
#     "c-Travel": []
# }
#
#
#
#
# for key,values in players_dict.items():
#     team = values.get("team")
#     status = values.get("status")
#     if team == "A" and status == "Rest":
#         sorted_dict.get("a-Rest").append(values.get("name"))
#     elif team == "B" and status == "Training":
#         sorted_dict.get("b-Training").append(values.get("name"))
#     elif team == "C" and status == "Travel":
#         sorted_dict.get("c-Travel").append(values.get("name"))
#
#
# for key,members in sorted_dict.items():
#     print(f"Команда: {key}")
#     for _members in members:
#         print(f"\tУчастники: {_members}")
#     print()





#способ через 3 списка:
# command_a_rest = []
# command_b_traning = []
# command_c_travel = []
#
#



# for values in players_dict.values():
#     team = values.get("team")
#     status = values.get("status")
#     if team == "A" and status == "Rest":
#         command_a_rest.append(values.get("name"))
#     elif team == "B" and status == "Training":
#         command_b_traning.append(values.get("name"))
#     elif team == "C" and status == "Travel":
#         command_c_travel.append(values.get("name"))
#
#
# print(f"Все члены команды А, которые отдыхают: {",".join(command_a_rest)}")
# print(f"Все члены команды B, которые тренируются: {",".join(command_b_traning)}")
# print(f"Все члены команды C, которые путешествуют: {",".join(command_c_travel)}")