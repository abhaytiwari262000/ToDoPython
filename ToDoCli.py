import os
import csv
from Task import Task

file_path = 'tasks.csv'

# Check if the file exists
if not os.path.exists(file_path):
    # Create the file and write the header + first row
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'task', 'status'])
        writer.writeheader()


print("Hello! Welcome to the ToDO app")

import csv

with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    tasks = list(reader)

# Sort: Put "Incomplete" tasks first
sorted_tasks = sorted(tasks, key=lambda x: x['status'] != 'pending')


maxId = 1
# print("Tasks (Pending First):")

for row in sorted_tasks:
    maxId = max(maxId, int(row['id']))
    # print(f"{row['id']}{row['task']} | Status: {row['status']}")

id = maxId+1

while(True):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        tasks = list(reader)

    # Sort: Put "Incomplete" tasks first
    sorted_tasks = sorted(tasks, key=lambda x: x['status'] != 'pending')
    print("Tasks (Pending First):")

    for row in sorted_tasks:
        print(f"{row['id']} {row['task']} | Status: {row['status']}")
    a = int(input('Press 1 to add task, 2 to update status of task, 3 to remove task, any other button to exit\n'))

    if(a==1):
        task = Task()
        task.name = input("Task name: ")
        task.id = id
        id+=1
        with open(file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file,fieldnames=['id','task','status'])
            writer.writerow({'id':task.id,'task':task.name,'status':'pending'})


    elif(a==2):

       updateId =  input("Please enter id of task to mark as done")

       with open(file_path, mode='r', newline='') as file:
           reader = csv.DictReader(file)
           rows = list(reader)

       for row in rows:
           if row['id'] == updateId:
               row['status'] = 'done'

       with open(file_path, mode='w', newline='') as file:
           fieldnames = ['id','task','status']
           writer = csv.DictWriter(file, fieldnames=fieldnames)
           writer.writeheader()
           writer.writerows(rows)

    elif(a==3):

        deleteId = int(input("Please enter id of task to delete"))

        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            fieldnames = reader.fieldnames


        rows = [row for row in rows if row['id']!=str(deleteId)]

        with open(file_path, mode='w',newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    else:
        break