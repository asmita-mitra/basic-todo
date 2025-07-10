import os
import json

file="task.json"

#Check if json file exists and load tasts, return empty list if not
def loadt():
    if os.path.exists(file):
        with open(file,"r") as f:
            return json.load(f)
    return []

#Save the tasks to the list
def savet(tasks):
    with open(file,"w") as f:
        json.dump(tasks,f,indent=2)

#Add a new task
def addt(title):
    tasks=loadt()
    tasks.append({"Task":title,"Status":"Not Done"})
    savet(tasks)

#Mark a task as done
def donet(index):
    tasks=loadt()
    if 0<=index<len(tasks):
        tasks[index]["Status"]="Done"
    savet(tasks)

#Remove task from the list
def deletet(index):
    tasks = loadt()
    if 0 <= index < len(tasks):
        del tasks[index]
        savet(tasks)