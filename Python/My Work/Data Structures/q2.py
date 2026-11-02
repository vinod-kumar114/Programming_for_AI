data = [("Fruit", "Apple"), ("Veg", "Carrot"), ("Fruit", "Mango"), ("Drink", "Cola"), ("Veg", "Peas")]

dic={}

for key, val in data:
    if key not in dic:
        dic[key] = []
    dic[key].append(val)
    
print(dic)