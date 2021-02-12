# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_data(name, surname, birthday, city, email, phone_number):
    return f'Name - {name}, surname - {surname}, birthday - {birthday}, city - {city},'  \
            f'email - {email}, phone - {phone_number}'

print(print_data(name='Jimm', surname='Smith', birthday='1992', city='Moscow', email='jimmy92@gmail.com', phone_number='89094455366'))

