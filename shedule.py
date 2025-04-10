import requests
def shedule_get():
    shedule = requests.get('https://nickly24-itclub-server-38c1.twc1.net/api/schedules')

    shedule_format = ""
    days_of_week = ['Понедельник', 'Вторник','Среда','Четверг','Пятница','Суббота']
    for w in days_of_week:
        shedule_format = shedule_format +'<b>'+ w +'</b>'+ '\n'
        for i in shedule.json():
            if i['day_of_week'] == w:
                shedule_format = shedule_format + i['name'] + " - " + i['time'][0:6] + '\n'
        shedule_format = shedule_format + '\n'
    return shedule_format