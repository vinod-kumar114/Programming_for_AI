# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)
# print(response.status_code)
# print(response)


# user = {
#     "name" : "Fatima",
#     "gmail": "Fatima@gmail.com"
# }

# response2 = requests.post(url, json=user)
# print(response2.status_code)

# response3 = requests.delete(url)
# print(response3.status_code)

import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)
if response.status_code == 200:
    dic = response.json()
    print(dic["name"])
    print(dic["email"])