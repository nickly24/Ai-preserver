import requests
from collections import defaultdict

def dnevnik_get(year, month, group_by_filial=True):
    response = requests.get(
        f'https://nickly24-itclub-server-453b.twc1.net/api//dnevnik/{year}/{month}',
        verify=False  # Отключает проверку SSL (небезопасно!)
    )
    
    if not response.ok:
        return response.json()  # Возвращаем как есть, если ошибка
    
    data = response.json()
    
    if not group_by_filial:
        # Простой формат без группировки
        simplified_data = []
        for entry in data:
            simplified_entry = {
                'filial_name': entry['filial_name'],
                'date': entry['date'],
                'number_of_children': entry['number_of_children'],
                'price_per_session': entry['price_per_session'],
                'earn': float(entry['price_per_session']) * entry['number_of_children']
            }
            simplified_data.append(simplified_entry)
        return simplified_data
    else:
        # Группировка по филиалам
        grouped_data = defaultdict(list)
        
        for entry in data:
            simplified_entry = {
                'date': entry['date'],
                'number_of_children': entry['number_of_children'],
                'earn': float(entry['price_per_session']) * entry['number_of_children']
            }
            grouped_data[entry['filial_name']].append(simplified_entry)
        
        # Преобразуем defaultdict в обычный dict для лучшей сериализации
        return dict(grouped_data)