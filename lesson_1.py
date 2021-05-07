import requests
import json

name = 'aguadoenzo'
url = 'https://api.github.com/users/' + name + '/repos'

response = requests.get(url)
if response.status_code == 200:
    j_data = json.loads(response.text)
    with open("repo_list.json", "w") as write_file:
        json.dump(j_data, write_file)
    print(f'Список репозиториев пользователя {name} выгружен.')
else:
    print(f'При выгрузке списка репозиториев пользователя {name} произошла ошибка: {response.status_code}.')