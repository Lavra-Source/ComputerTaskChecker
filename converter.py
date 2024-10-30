import site
import ntpath

import os
import sys
import json
site.addsitedir('./code')  # Always appends to end
print(sys.path)
d = dict()
tasks = []
def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
        d["content"] = open(path, 'r').read()

    return d

if __name__ == "__main__":
    print("input number of tasks")
    n = int(input())
    for i in range(n):
        print("arrange the files properly and type in the task description, then hit Enter")
        description = input()
        tasks.append([description, path_to_dict('./work')])
    with open("result.json", 'w') as file:
        file.write(json.dumps(tasks))
print (json.dumps(tasks))