
# import requests
# import time


# API_URL = 'https://api.telegram.org/bot'
# BOT_TOKEN = '6850289793:AAGh_f5obILLX0qd5tecl5BIkBqZC-Parpw'
# TEXT = 'Ура! Классный апдейт!'
# MAX_COUNTER = 100

# offset = -2
# counter = 0
# chat_id: int


# while counter < MAX_COUNTER:

#     print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

#     time.sleep(1)
#     counter += 1


import requests
import time

api_url = 'https://api.telegram.org/bot'
api_cat_url = 'https://api.thecatapi.com/v1/images/search'
api_dog_url = 'https://random.dog/woof.json'
api_fox_url = 'https://randomfox.ca/floof/'
token = '5788580379:AAExLisvcziFci2k2zoZ-XEtCwqwZow3YPc'
error = 'Ты лох. Пиши: собачка, котик, лисичка'
loh ='Нет, ты лох, соси яйца'
vika = 'Вика, иди работай'

offset = -2

cat_response: requests.Response
cat_link: str
fox_response: requests.Response
fox_link: str
dog_response: requests.Response
dog_link: str
counter = 0



while counter < 100:
  
    updates = requests.get(f'{api_url}{token}/getUpdates?offset={offset + 1}').json()
    print(counter)
    
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(api_cat_url)
            dog_response = requests.get(api_dog_url)
            fox_response = requests.get(api_fox_url)
            if (result['message']['text']).lower() == 'котик':
                if cat_response.status_code == 200:
                    cat_link = cat_response.json()[0]['url']
                    requests.get(f"{api_url}{token}/sendPhoto?chat_id={chat_id}&photo={cat_link}")
            elif (result['message']['text']).lower() == 'лисичка':
                if fox_response.status_code == 200:
                    response = requests.get(api_fox_url)
                    fox_link = response.json()['image']
                    requests.get(f"{api_url}{token}/sendPhoto?chat_id={chat_id}&photo={fox_link}")
            elif (result['message']['text']).lower() == 'собачка':
                if dog_response.status_code == 200:
                    response = requests.get(api_dog_url)
                    dog_link = response.json()['url']
                    requests.get(f"{api_url}{token}/sendPhoto?chat_id={chat_id}&photo={dog_link}")
            elif (result['message']['text']).lower() in ['игорь лох', "сам лох", "лох", "ты лох"]:
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text={loh}')
                
            elif (result['message']['text']).lower() in ['какашки', "говно", "пися", "попа", "кал", "моча", "пенис", "жопа", "мама"]:
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text={vika}')
                

            else:
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text={error}')
    time.sleep(1)
    # counter += 1
