import requests
import json
import csv

url="https://jsonplaceholder.typicode.com/comments"

try:
    post_id=input("Enter post id: ")

    response=requests.get(url,params={"postId":post_id},timeout=5)

    print("status code:",response.status_code)

    response.raise_for_status()

    data=response.json()

    if len(data)>0:
        results=[]

        for item in data:
            results.append({
                "name":item["name"],
                "email":item["email"],
                "text":item["body"]
            })

        print("retrieved data:")
        for item in results:
            print(item)

        print("total results:",len(results))

        with open("results.json","w") as f:
            json.dump(results,f,indent=4)

        with open("results.csv","w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["name","email","text"])

            for item in results:
                writer.writerow([item["name"],item["email"],item["text"]])

        print("data saved successfully.")

    else:
        print("no results found.")

except requests.exceptions.Timeout:
    print("request timed out.")

except requests.exceptions.ConnectionError:
    print("connection error.")

except requests.exceptions.HTTPError:
    print("http error occurred.")

except FileNotFoundError:
    print("file does not exist.")

except json.JSONDecodeError:
    print("invalid json data.")

except requests.exceptions.RequestException as error:
    print("request failed:",error)

else:
    try:
        with open("results.json","r") as f:
            saved_data=json.load(f)

        print("json file verified:")
        print(saved_data)

        with open("results.csv","r") as f:
            reader=csv.reader(f)

            print("csv file verified:")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("file does not exist.")

    except json.JSONDecodeError:
        print("invalid json data.")

finally:
    print("program finished.")
