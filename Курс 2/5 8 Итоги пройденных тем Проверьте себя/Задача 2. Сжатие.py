text = input("Введите строку: ")
text_coder = ""
current_char = text[0]
count = 1
for char in text[1:]:
    if char == current_char:
        count += 1
    else:
        text_coder += current_char + str(count)
        current_char = char
        count = 1
print(f"Закодированная строка: {text_coder}")