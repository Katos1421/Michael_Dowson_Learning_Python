# Программа "Пароль"
# Демонстрирует работу функции if

print('Добро пожаловать в Security Incorporated. Все что мы можем - это спрашивать пароли у людей.')
input('--Безопасность наше второе имя\n')

password = input('Введите пароль:')
if password == "secret":
    print('Доступ открыт!')

input('\nНажмите Enter, чтобы выйти')