import requests

def getObjects():
    urlRandomJokes = "https://api.chucknorris.io/jokes/random"
    jokes = {}

    for i in range(25):
        with requests.Session().get(urlRandomJokes) as response:
            getRandomJokes = response.json()
            jokes.update({getRandomJokes['id']:getRandomJokes['value']})


            if jokes[getRandomJokes['id']] == getRandomJokes['id']:
                jokes.pop(getRandomJokes['id'])
    
    return jokes

getObjects()
    
    



