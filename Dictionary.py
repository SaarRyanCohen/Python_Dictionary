import requests

with open('dict.txt' , 'a+') as file:
    word = input('please enter a word you wish to define: ')

    print(word)

    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+word

    response = requests.get(url)
    response_json = response.json()
    file.write(response_json[0]['word'] +' : ')
    file.write(response_json[0]['meanings'][0]['definitions'][0]['definition'] + '\n\n')