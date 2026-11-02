# episodes = ["Origin", "Signals", "The Hidden Code", "After Midnight", "Future Lab", "Deep Space", "Final Call"]

# # print(episodes[:3])
# # print(episodes[3:4])

# reverse = []
# for i in episodes[len(episodes)-1:0:-1]:
#     reverse.append(i)

# # print(reverse)

# categories = ["AI", "Science", "AI", "Travel", "Science", "Music"]
# unique_categories = set(categories)

# # print(unique_categories)

# c=0
# for i in categories:
#     if i.lower() == 'science':
#         c+=1
# # print("Scince appears",c,"times")


# records = [{"room":"101", "guests":["Ali","Sara"]}, {"room":"204", "guests":["Hina"]},{"room":"101", "guests":["Usman","Zoya","Hamza"]}, {"room":"305", "guests":["Billal","Areeb"]}]

# # z = records[2]["guests"][1]
# # print(z)

# # for record in records:
# #     for key, value in record.items():
# #         print(key,":",value)

# room_users={}
# for record in records:
#     room=record["room"]
#     guests = record["guests"]
#     if room in room_users:
#         room_users[room].extend(guests)
#     else:
#         room_users[room]=list(guests)

# # print(room_users)
# full_rooms=[]
# for room, guests in room_users.items():
#     if len(guests)>=3:
#         full_rooms.append(room)

# # print(full_rooms)

# unique_people = set()
# for guest in room_users.values():
#     for person in guest:
#         unique_people.add(person)

# print(unique_people)

# large_room = None
# lent=-1

# for key, value in room_users.items():
#     if len(value)>lent:
#         lent=len(value)
#         large_room=key

# print(large_room)

tags = ["python", "ai", "python", "nlp", "vision", "ai", "python", "data"]

dic = {}
for i in tags:
    dic[i]=dic.get(i, 0)+1

print(dic)

repeated_tags=[]
for key, val in dic.items():
    if val>1:
        repeated_tags.append(key)

print(repeated_tags)