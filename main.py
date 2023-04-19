import requests

response = requests.get('https://www.flashscore.com/')

print('Status Code: ', response.status_code)
print('Headers: ')
print(response.headers)
print('\n Content')
print(response.content)
