import requests

def filials_get():
    response = requests.get(
        'https://nickly24-itclub-server-38c1.twc1.net/api/filials',
        verify=False  # Отключает проверку SSL (небезопасно!)
    )
    data = []
    for i in response.json():
        data.append({
            'id': i['id'],
            'name': i['name'],
            'address': i['address'],
            'metro': i['metro'],
        })
    return data
