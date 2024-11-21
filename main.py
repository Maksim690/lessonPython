#TODO Задание 2
while True:
    password = input("Введите пароль:")
    if len(password) <= 8:
        print("Короткий")
        continue
    if "123" in password:
        print('Простой')
        continue
    else:
        print("Хорошо")
        break