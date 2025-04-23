import site
import sys
import json
site.addsitedir('./code')  # Always appends to end
from checker import path_to_dict
d = dict()
tasks = []
sys.stdin.reconfigure(encoding='utf-8-sig')
sys.stdout.reconfigure(encoding='utf-8-sig')


if __name__ == "__main__":
    print("input number of subtasks")
    n = int(input())
    for i in range(n):
        input("Initial state")
        dict1 = path_to_dict('./work')
        input("Target state and description")
        description = open("desc.txt", 'r', encoding="utf-8-sig").read()
        image = input("image file path")
        tasks.append([description, dict1, path_to_dict('./work'), image])
    with open("Tasks/Task1.json", 'w', encoding = "utf-8-sig") as file:
        file.write(json.dumps(tasks))
print (json.dumps(tasks))