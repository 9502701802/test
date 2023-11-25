import requests

def get_data(query):
    url = ' https://api.ambeedata.com/latest/by-city?city=' + query + '&x-api-key=1bbc8933a3e1bdf2183efe42a8574e0b641a58556381aceb52acb43b1266eaa5'
    response = requests.get(url)
    return response.status_code, response.json()