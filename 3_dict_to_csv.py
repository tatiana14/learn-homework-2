import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    users = [{'name': 'Matias', 'age': 99, 'job': 'retired'},
              {'name': 'Anna', 'age': 79, 'job': 'chief'},
              {'name': 'Taru', 'age': 59, 'job': 'rector'},
              {'name': 'Rita', 'age': 39, 'job': 'teacher'}
              ]
    with open('users.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in users:
            writer.writerow(user)


if __name__ == "__main__":
    main()
