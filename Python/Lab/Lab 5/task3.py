import json
import os

file = "model_results.json"

def add(name, accuracy, precision, recall, f1):
    with open(file, "w") as f:
        json.dump([], f)

    with open(file, "r") as f:
        models =json.load(f)

    models.append({
        "model": name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    })

    with open(file, "w") as f:
        json.dump(models, f, indent=4)

def display():
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r") as f:
        models = json.load(f)

    for model in models:
        print(model)

def highest_accuracy():
    with open(file, "r") as f:
        models = json.load(f)

    highest = models[0]

    for model in models:
        if model["accuracy"] > highest["accuracy"]:
            highest = model

    print("highest accuracy model:", highest["model"])

def highest_f1():
    with open(file, "r") as f:
        models = json.load(f)

    highest = models[0]

    for model in models:
        if model["f1"] > highest["f1"]:
            highest = model

    print("highest f1 model:", highest["model"])

def update(name, accuracy, precision, recall, f1):
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r") as f:
        models = json.load(f)

    found = False

    for model in models:
        if model["model"] == name:
            model["accuracy"] = accuracy
            model["precision"] = precision
            model["recall"] = recall
            model["f1"] = f1
            found = True

    with open(file, "w") as f:
        json.dump(models, f, indent=4)

    if found:
        print("model updated successfully.")
    else:
        print("model does not exist.")

def remove(name):
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r") as f:
        models = json.load(f)

    new_models = []
    found = False

    for model in models:
        if model["model"] == name:
            found = True
        else:
            new_models.append(model)

    with open(file, "w") as f:
        json.dump(new_models, f, indent=4)

    if found:
        print("model removed successfully.")
    else:
        print("model does not exist.")


if not os.path.exists(file):
    models = [
        {
            "model": "linear regression",
            "accuracy": 0.85,
            "precision": 0.82,
            "recall": 0.80,
            "f1": 0.81
        },
        {
            "model": "decision tree",
            "accuracy": 0.90,
            "precision": 0.88,
            "recall": 0.87,
            "f1": 0.87
        },
        {
            "model": "neural network",
            "accuracy": 0.94,
            "precision": 0.92,
            "recall": 0.91,
            "f1": 0.91
        }
    ]

    with open(file, "w") as f:
        json.dump(models, f, indent=4)

print("model results:")
display()

print("highest accuracy:")
highest_accuracy()

print("highest f1:")
highest_f1()

add("random forest", 0.92, 0.90, 0.89, 0.89)

print("after adding:")
display()

update("decision tree", 0.93, 0.91, 0.90, 0.90)

print("after updating:")
display()

remove("linear regression")

print("after removing:")
display()