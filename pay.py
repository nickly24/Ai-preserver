from filials import filials_get
import datetime as dt 
class Pay:
    
    import requests
    #https://nickly24-itclub-server-453b.twc1.net/api/analytics/{year}/{month}/{filial_id}
    url = 'https://nickly24-itclub-server-453b.twc1.net/api/analytics/'
    a = dt.datetime.today().date()
    yy = a.year
    mm = a.month
    dd = a.day
    def thispol(self,filial_id):
        a = dt.datetime.today().date()
        yy = a.year
        mm = a.month
        filials = filials_get()
        filial_name = None
        for i in filials:
            if i['id'] == filial_id:
                filial_name = i['name']
        if self.dd > 15:
            url = self.url + str(yy) + '/' + str(mm) + '/' + str(filial_id)
            res = self.requests.get(url).json()
            summ = 0
            answer = f'Счет для {filial_name} за текущий полумесяц: \n'
            for i in res:
                if int(i['date'][8:10]) > 15:
                    this_date = i['date'][8:10]+'.'+i['date'][5:7]
                    ppl = int(i['number_of_children'])
                    price = int(i['price_per_session'][0:3])
                    line_summ = ppl*price
                    summ += line_summ
                    line = f'{this_date} - {ppl} чел. => {line_summ} руб'
                    answer += line + '\n'
            answer += f'Общая сумма: {summ} руб'
            return answer
        else:
            url = self.url + str(yy) + '/' + str(mm) + '/' + str(filial_id)
            res = self.requests.get(url).json()
            summ = 0
            answer = f'Счет для {filial_name} за текущий полумесяц: \n'
            for i in res:
                if int(i['date'][8:10]) <= 15:
                    this_date = i['date'][8:10]+'.'+i['date'][5:7]
                    ppl = int(i['number_of_children'])
                    price = int(i['price_per_session'][0:3])
                    line_summ = ppl*price
                    summ += line_summ
                    line = f'{this_date} - {ppl} чел. => {line_summ} руб'
                    answer += line + '\n'
            answer += f'Общая сумма: {summ} руб'
            return answer
    def prevpol(self,filial_id):
        a = dt.datetime.today().date()
        yy = a.year
        mm = a.month
        filials = filials_get()
        filial_name = None
        for i in filials:
            if i['id'] == filial_id:
                filial_name = i['name']
        if self.dd > 15:
            url = self.url + str(yy) + '/' + str(mm) + '/' + str(filial_id)
            res = self.requests.get(url).json()
            summ = 0
            answer = f'Счет для {filial_name} за текущий полумесяц: \n'
            for i in res:
                if int(i['date'][8:10]) <= 15:
                    this_date = i['date'][8:10]+'.'+i['date'][5:7]
                    ppl = int(i['number_of_children'])
                    price = int(i['price_per_session'][0:3])
                    line_summ = ppl*price
                    summ += line_summ
                    line = f'{this_date} - {ppl} чел. => {line_summ} руб'
                    answer += line + '\n'
            answer += f'Общая сумма: {summ} руб'
            return answer
        else:
            url = self.url + str(yy) + '/' + str(mm-1) + '/' + str(filial_id)
            res = self.requests.get(url).json()
            summ = 0
            answer = f'Счет для {filial_name} за текущий полумесяц: \n'
            for i in res:
                if int(i['date'][8:10]) > 15:
                    this_date = i['date'][8:10]+'.'+i['date'][5:7]
                    ppl = int(i['number_of_children'])
                    price = int(i['price_per_session'][0:3])
                    line_summ = ppl*price
                    summ += line_summ
                    line = f'{this_date} - {ppl} чел. => {line_summ} руб'
                    answer += line + '\n'
            answer += f'Общая сумма: {summ} руб'
            return answer
    def thismonth(self,filial_id):
        a = dt.datetime.today().date()
        yy = a.year
        mm = a.month
        filials = filials_get()
        filial_name = None
        for i in filials:
            if i['id'] == filial_id:
                filial_name = i['name']
        url = self.url + str(yy) + '/' + str(mm) + '/' + str(filial_id)
        res = self.requests.get(url).json()
        summ = 0
        answer = f'Счет для {filial_name} за текущий месяц: \n'
        for i in res:
            this_date = i['date'][8:10]+'.'+i['date'][5:7]
            ppl = int(i['number_of_children'])
            price = int(i['price_per_session'][0:3])
            line_summ = ppl*price
            summ += line_summ
            line = f'{this_date} - {ppl} чел. => {line_summ} руб'
            answer += line + '\n'
        answer += f'Общая сумма: {summ} руб'
        return answer
    def prevmonth(self,filial_id):
        a = dt.datetime.today().date()
        yy = a.year
        mm = a.month
        filials = filials_get()
        filial_name = None
        for i in filials:
            if i['id'] == filial_id:
                filial_name = i['name']
        url = self.url + str(yy) + '/' + str(mm-1) + '/' + str(filial_id)
        res = self.requests.get(url).json()
        summ = 0
        answer = f'Счет для {filial_name} за прошлый месяц: \n'
        for i in res:
            this_date = i['date'][8:10]+'.'+i['date'][5:7]
            ppl = int(i['number_of_children'])
            price = int(i['price_per_session'][0:3])
            line_summ = ppl*price
            summ += line_summ
            line = f'{this_date} - {ppl} чел. => {line_summ} руб'
            answer += line + '\n'
        answer += f'Общая сумма: {summ} руб'
        return answer
