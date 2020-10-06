import hashlib #voor de hash
import urllib.parse
import requests  #voor de requests
import datetime  #voor de timestamp

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
PUBLIC_KEY = "3b647296b973547fcc40f00249c5be8e"
PRIVATE_KEY = "9692ed4ee5bc8e6ce16eb97a384e6c5d99ef4580"
main_api = "https://gateway.marvel.com:443/v1/public/characters"

def hash_params():
    #dit zorgt voor de hashes  

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{PRIVATE_KEY}{PUBLIC_KEY}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


while True:   
    Character = input(" Over welke character wil je meer info over weten:" )
    params = {'name':  Character, 'ts': timestamp,'apikey': PUBLIC_KEY, 'hash': hash_params()};
    request = requests.get(main_api,params=params)
    json_data = request.json()
    json_status = json_data["code"]

    

    if Character == "quit" or Character == "q":
        break

    if json_status == 200:
        print()
        print("URL: " + (main_api + '?' + urllib.parse.urlencode(params)))
        print("API status: " + str(json_status) + " = Succesful call.\n")
        print("========================================================")
        print("Name: " + (json_data["data"]["results"][0]["name"]))
        print("Description: " + (json_data["data"]["results"][0]["description"]))
        print("======================================================== \n")
   
    #error json_status weergeven en zeggen wat er fout is
    elif json_status == 409:
        print("*******************************************************")
        print("Status code: " + str(json_status) + "; Missing API key ")
        print("*******************************************************")
    elif json_status == 401:
        print("**************************************************************")
        print("Status code: " + str(json_status) + "; Invalid referer or hash")
        print("**************************************************************")
    elif json_status == 405:
        print("*********************************************************")
        print("Status code: " + str(json_status) + "; Method not allowed")
        print("*********************************************************")
    elif json_status == 403:
        print("************************************************")
        print("Status code: " + str(json_status) + "; Forbidden")
        print("************************************************")


