# Это тестовый файл с тестовыми функциями


# функция приветствия
def welcome(name):
    print(f'Hello, {name}. How old are you?')


# функция ответа с возрастом
def answer_age(age):
    print(f'Hello, I am {age} years old.')


if __name__ == '__main__':
    welcome('Sonya')
    answer_age(25)
