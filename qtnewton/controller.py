# docstring and imports, todo
import requests

BASE_URL = "https://newton.now.sh/api/v2/"

if __name__ == "__main__":
    # testing api
    endpoint = "derive/"
    argument1 = "x^2"
    argument2 = None # Usually unused but some endpoints need a third argument in the middle of the others
    argument3 = None # Some endpoints need a second argument

    url = BASE_URL + endpoint + argument1
    if argument2 != None:
        url += ':' + argument2
    if argument3 != None:
        url += '|' + argument3

    response = requests.get(url)
    if response.ok:
        print(response.text)
        results = dict(response.json())
    else:
        print("Error")