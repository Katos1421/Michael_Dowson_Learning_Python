# Компьютерный датчик настроения
# Демонстрирует работу функции elif
import random
print('Я ощущаю вашу энергетику. От моего экрана не скрыто ни одно из ваших чувств...')
print('Итак, ваше настроение...')
mood = random.randint(1, 3)

if mood == 1:
       #радостное
       print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)
elif mood == 2:
       #нейтральное
       print( \
           """
              -----------
              |         |
              | O    O  |
              |   <     |
              |         |
              | ------  |
              |         |
              -----------
                          """)
elif mood == 3:
       #грустное
       print( \
           """
              -----------
              |         |
              | O    O  |
              |   <     |
              |         |
              |  .'.    |
              | '   '   |
              -----------
                          """)
else:
    print('Не бывает такого настроения! (Должно быть вы совершенно не в себе)')
print ('Но это только сегодня...')

input('\nНажмите Enter, чтобы выйти')
