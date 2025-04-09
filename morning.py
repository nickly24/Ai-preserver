import requests
import datetime
def morning_mes():
    now = datetime.datetime.today()
    today = now.weekday()
    shedule = requests.get('https://nickly24-itclub-server-453b.twc1.net/api/schedules')
    days = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    day = days[today]
    S = []
    for i in shedule.json():
        if i['day_of_week'] == day:
            S.append(i)

    def F(e):
        a = int(e['time'][0]+e['time'][1]+e['time'][3]+e['time'][4])
        return a

    S.sort(key=F)
    answer = 'Доброе утро! Занятия на сегодня: \n \n'
    for i in S:
        answer = answer + '<b>' + i['name'] + '</b>' + ' - ' +i['time'][0:5] + '\n'
        answer = answer + '''<i style="color: ''' +i['metro_color'] + '''">Метро:'''  +i['metro'] + '</i> \n'
        answer = answer + '<i>Адресс: ' +i['address'] + '</i> \n \n'
    return answer