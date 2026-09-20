import json

class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed


hw_list = [
    Homework("Lap trinh App Producer", 3),
    Homework("Lam van", 2, True),
    Homework("Lap trinh GameMaker", 3)
]

for item in hw_list:
    print(item.name, item.priority, item.completed)

data = []

for item in hw_list:
    data.append({
        "name": item.name,
        "priority": item.priority,
        "completed": item.completed
    })

with open("homework.json", "w") as file:
    json.dump(data, file, indent=4)

print("Da luu!")