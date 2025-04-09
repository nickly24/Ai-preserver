from flask import Flask, jsonify, request
from filials import filials_get
from analytic import analytic_get
from shedule import shedule_get
from dnevnik import dnevnik_get
app = Flask(__name__)

@app.route('/filials')
def index():
    
    return jsonify(filials_get)



@app.route('/analytics', methods=['POST'])
def get_analytics():
    # Получаем JSON-данные из тела запроса
    data = request.get_json()

    # Проверяем, что все нужные поля есть
    if not data or 'year' not in data or 'month' not in data:
        return jsonify({"error": "Не хватает параметров (year, month)"}), 400

    year = data['year']
    month = data['month']
    # Вызываем функцию получения аналитики
    analytics = analytic_get(year, month)
    # Возвращаем JSON-ответ
    return jsonify(analytics)

@app.route('/shedule')
def get_shedule():
    # Вызываем функцию получения расписания
    shedule = shedule_get()
    # Возвращаем JSON-ответ
    return jsonify(shedule)

@app.route('/dnevnik', methods=['POST'])
def get_dnevnik():
    # Получаем JSON-данные из тела запроса
    data = request.get_json()
    year = data['year']
    month = data['month']
    # Проверяем, что все нужные поля есть
    if not data or 'year' not in data or 'month' not in data:
        return jsonify({"error": "Не хватает параметров (year, month)"}),
    # Вызываем функцию получения дневника
    dnevnik = dnevnik_get(year, month)
    # Возвращаем JSON-ответ
    return jsonify(dnevnik)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 