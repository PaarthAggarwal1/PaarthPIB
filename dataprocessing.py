import json

with open("data.json", "r") as file:
    data = json.load(file)

user_ids = set()
users = []

for user in data:
    if user["user_id"] not in user_ids:
        user_ids.add(user["user_id"])
        users.append(user)

for user in users[:]:
    if user["score"] < 50:
        users.remove(user)

scores = [user["score"] for user in users]

print("Average score:", sum(scores) / len(scores))
print("Maximum score:", max(scores))
print("Minimum score:", min(scores))

top_users = sorted(users, key=lambda x: x["score"], reverse=True)

print("Top 10 users:")
for user in top_users[:10]:
    print(user)
