import requests
import json

params = {'user_ids': '210700286',
          'fields': 'bdate',
          'access_token': '418b766c418b766c418b766c7141fcb7a24418b418b766c211e267a14b0abf5c18f98c6',
          'v': '5.130'}

url = 'https://api.vk.com/method/users.get'

response = requests.get(url, params=params)
if response.status_code == 200:
    j_data = json.loads(response.text)
    with open("vc_info.json", "w") as write_file:
        json.dump(j_data, write_file)
    print(f'Данные пользователя выгружены.')
else:
    print(f'При выгрузке данных пользователя произошла ошибка: {response.status_code}.')