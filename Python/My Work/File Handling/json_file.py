

# # json.dump(): Python Dict/List ko JSON File mein save karna.

# # json.load(): JSON File se data read karke Python Dict/List mein convert karna.

# # json.dumps(): Python Dict ko JSON String (Text) mein convert karna (s = string).

# # json.loads(): JSON String ko Python Dict mein convert karna.


# import json

# student_data = {
#     "name": "Ali",
#     "age": 20,
#     "is_enrolled": True,
#     "subjects": ["Python", "NumPy", "Data Science"],
#     "address": {
#         "city": "Karachi",
#         "zip": 75500
#     }
# }


# # Saving data : json.dump()
# with open("student.json","w") as file:
#     json.dump(student_data,file,indent=4)

# # reading data: json.load()
# with open("student.json","r") as file:
#     print(json.load(file))


# # working with strings: loads and dumps

# user_dict = {"name":"ahmed", "status":"active"}
# json_str = json.dumps(user_dict)
# print(json_str)

# json_data = '{"name": "Sara", "score": 95}'
# python_data = json.loads(json_data)
# print(python_data)



import json

models_data = [
    {"model": "CNN", "accuracy": 0.88, "f1_score": 0.85},
    {"model": "ResNet", "accuracy": 0.94, "f1_score": 0.92},
    {"model": "ViT", "accuracy": 0.91, "f1_score": 0.89}
]

with open("model_results.json", "w") as file:
    json.dump(models_data,file, indent=4)


md = None
maxAcc = 0
with open("model_results.json", "r") as file:
    data = json.load(file)

    for item in data:
        if item["accuracy"] >maxAcc:
            maxAcc=item["accuracy"]
            md = item["model"]