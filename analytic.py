import requests
from filials import filials_get
def analytic_get(year,month):
    answer = ""
    filials = filials_get()
    locals_sum = 0
    for sad in filials:
        if sad['name'] != 'B2O6' and sad['name'] != 'Аленушка Боровское' and sad['name'] != 'Teeny Weeny':
            
            filial_id = sad['id']

            # Формируем URL запроса
            url = f"https://nickly24-itclub-server-453b.twc1.net/api/analytics/{year}/{month}/{filial_id}"

            # Отправляем GET-запрос
            response = requests.get(url,verify=False )

            # Проверяем статус ответа
            if response.status_code == 200:
                # Получаем данные из ответа
                data = response.json()
                #print('work')  # Выводим полученные данные
            else:
                print(f"Ошибка: {response.status_code}")
            s = 0
            for i in data:
                s += int(i['price_per_session'][0:3]) * int(i['number_of_children'])
            if s>0:
                answer = answer + "<b>" +sad['name']+"</b>\n"
                answer = answer + str(s) + ' рублей \n\n'
                locals_sum += s
    answer+= 'Общая сумма - '+str(locals_sum)
    return answer
