import requests

url="https://jsonplaceholder.typicode.com/users"

try:
    response=requests.get(url,timeout=5)
    print("get status code:",response.status_code)
    print("get response:",response.json())

    user={"name":"Ali","email":"ali@gmail.com"}
    response = requests.post(url,json=user,timeout=5)
    print("post status code:",response.status_code)
    print("post response:",response.json())

    url2="https://jsonplaceholder.typicode.com/users/1"
    user={"name":"Ahmed","email":"ahmed@gmail.com"}

    response=requests.put(url2,json=user,timeout=5)
    print("put status code:",response.status_code)
    print("put response:",response.json())

    response=requests.delete(url2,timeout=5)
    print("delete status code:",response.status_code)

except requests.exceptions.Timeout:
    print("request timed out.")

except requests.exceptions.ConnectionError:
    print("connection error.")

except requests.exceptions.HTTPError:
    print("http error occurred.")

except ValueError:
    print("invalid response.")

except requests.exceptions.RequestException as error:
    print("request failed:",error)
