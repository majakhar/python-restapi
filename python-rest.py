#/usr/bin/env python3

# requests module make it easy to send HTTP(HYPER TEXT TRANSFER PROTOCOL) requests.
# Data flow: 
#      client: requests(create http request) --> socket(send bytes using socket to the server)  


import requests

def send_get_request():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    print(response.status_code)
    print(response.headers)
    return response.json()

print(send_get_request())