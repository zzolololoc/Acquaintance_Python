"""
Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу.

Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования.
Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.
"""

# кодер
def encryption(text, shift):
    alfavit = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    encryption_result = []
    for i in text.lower():
        if i not in alfavit:
          encryption_result.append(i)
        else:
            encryption_result.append(alfavit[alfavit.index(i) + shift])
    return encryption_result

# решил еще сразу декодер сделать
def decoder(text, shift):
    password = "124"
    while True:
        password_user = int(input("Введите пароль: "))
        if password_user == int(password):
            return encryption(text, -shift)
        else:
            print("Неверный пароль!")


text = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

encryption_result = encryption(text,shift)

print("".join(encryption_result))
decoder_copy = "".join(encryption_result)


decoder_result = decoder(decoder_copy,shift)
print(f"Расшифровка: {''.join(decoder_result)}")



