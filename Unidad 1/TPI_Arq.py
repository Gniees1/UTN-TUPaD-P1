import requests

url = "http://127.0.0.1:5000/flores"  

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Lista de flores:")
    for flor in data:
        print(flor)
else:
    print("Error en la petición:", response.status_code)
