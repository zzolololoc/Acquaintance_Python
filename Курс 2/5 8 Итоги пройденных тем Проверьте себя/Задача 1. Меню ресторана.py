menu = "утиное филе;фланк-стейк;банановый пирог;плов"
menu = ", ".join([men.title() for men in menu.split(";")])
print(menu)