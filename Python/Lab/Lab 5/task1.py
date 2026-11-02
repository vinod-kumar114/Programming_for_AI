import os

file = "experiments.txt"

def add(id, model, dataset, lr, epochs):
    with open(file, "a") as f:
        f.write(f"{id},{model},{dataset},{lr},{epochs}\n")

def display():
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r") as f:
        for line in f:
            print(line.strip())

def search(eid):
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == str(eid):
                print("Experiment found:")
                print("ID:", data[0])
                print("Model:", data[1])
                print("Dataset:", data[2])
                print("Learning Rate:", data[3])
                print("Epochs:", data[4])
                return

    print("Experiment does not exist.")

def update(id, model, dataset, lr, epochs):
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r") as f:
        lines = f.readlines()

    found = False

    with open(file, "w") as f:
        for line in lines:
            data = line.strip().split(",")

            if data[0] == str(id):
                f.write(f"{id},{model},{dataset},{lr},{epochs}\n")
                found = True
            else:
                f.write(line)

    if found:
        print("Experiment updated successfully.")
    else:
        print("Experiment does not exist.")

def remove_exp(id):
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r") as f:
        lines = f.readlines()

    found = False

    with open(file, "w") as f:
        for line in lines:
            data = line.strip().split(",")

            if data[0] == str(id):
                found = True
            else:
                f.write(line)

    if found:
        print("Experiment removed successfully.")
    else:
        print("Experiment does not exist.")


if not os.path.exists(file):
    with open(file, "w") as f:
        f.write("")

add(1, "Linear Regression", "Housing", 0.01, 100)
add(2, "Decision Tree", "Diabetes", 0.05, 150)
add(3, "Neural Network", "Images", 0.001, 200)

print("Experiment Configurations:")
display()

print("\nSearching Experiment:")
search(2)

add(4, "Random Forest", "Cancer", 0.02, 120)

print("\nAfter Adding New Experiment:")
display()

update(2, "Decision Tree", "Diabetes", 0.01, 200)

print("after updating:")
display()

remove_exp(3)

print("after removing:")
display()
