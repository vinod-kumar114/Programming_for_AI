products = [{"id":"P01","name":"mouse","prices":[1200,1350], "tags":["tech","usb"]}, {"id":"P02","name":"keyboard","prices":[2500,2800], "tags":["tech","office"]}, {"id":"P03","name":"notebook","prices":[450,500],"tags":["office","paper"]},{"id":"P04","name":"headset","prices":[3200,3500], "tags":["tech","audio"]}]

name = []
for product in products:
    name.append(product["name"])

print(name)
sum=0
for product in products:
    for i in product["prices"]:
        sum+=i

# print("Avg: ", sum/len(products))

unique_tags = set()
for product in products:
    for i in product["tags"]:
        unique_tags.add(i)

print(unique_tags)