import requests

url="https://jsonplaceholder.typicode.com/users"

try:
    name=input("Enter user name: ")
    response = requests.get(url, params={"name":name}, timeout=5)

    print("status code:",response.status_code)

    response.raise_for_status()

    data=response.json()

    if len(data)>0:
        user=data[0]

        print("prediction result:",user["name"])
        print("confidence score:",user["id"])
        print("input information:",user["email"])
    else:
        print("requested result not found.")

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



# use this user name: Leanne Graham