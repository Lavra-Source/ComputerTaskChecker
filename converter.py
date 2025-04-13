import site
import ntpath

import os
import sys
import json
site.addsitedir('./code')  # Always appends to end
print(sys.path)
d = dict()
tasks = []
sys.stdin.reconfigure(encoding='utf-8-sig')
sys.stdout.reconfigure(encoding='utf-8-sig')
def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        d["content"] = open(path, 'r', encoding="utf-8-sig").read()

    return d

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