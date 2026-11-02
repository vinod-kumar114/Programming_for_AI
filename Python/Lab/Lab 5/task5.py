import requests
import json
import csv

url="https://jsonplaceholder.typicode.com/comments"

try:
    query=input("Enter post id: ")
    response = requests.get(url,params={"postId":query},timeout=5)

    print("status code:",response.status_code)

    response.raise_for_status()

    data=response.json()

    if len(data)>0:
        print("retrieved results:")

        for item in data:
            print("text:",item["body"])
            print("author/source:",item["email"])
            print("name:",item["name"])

        with open("text_data.json","w") as f:
            json.dump(data,f,indent=4)

        with open("text_data.csv","w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["name","email","text"])

            for item in data:
                writer.writerow([item["name"],item["email"],item["body"]])

        print("data saved successfully.")
    else:
        print("no results found.")

except requests.exceptions.Timeout:
    print("request timed out.")

except requests.exceptions.ConnectionError:
    print("connection error.")

except requests.exceptions.HTTPError:
    print("http error occurred.")

except ValueError:
    print("invalid response.")

except OSError:
    print("file error.")

except requests.exceptions.RequestException as error:
    print("request failed:",error)


# Use post id: 1