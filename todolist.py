import pandas as pd
import datetime

# index = []
task = []
status = []
createdAt = []
completedAt = []

# for i in range(1, len(task) - 1):
#     index.append(str(i))

todo = {"Task": task, "Status": status, "Created At": createdAt, "Completed At": completedAt}

df = pd.DataFrame(todo)
#dataframe = df.style.hide_index_()
dataframe = df.style.hide(axis="index")

def addTask():
    addTaskInput = input("Enter the task you wish to add to your todo list: ")
    task.append(addTaskInput)
    createdAt.append(str(datetime.datetime.now()))
    status.append("False")
    return "Task added successfully!\n", dataframe

def viewTask():
    #pendinf task
    return dataframe

def editTask():
    edit = int(input("Enter the # No. of the task you wish to edit: "))
    
    return

def deleteTask():
    return

def markAsDone():
    return

def menu():
    while True:
        print("MENU\n1. Add new task \n2. View tasks \n3. Edit/Delete task \n4. Mark a task done \n5. Exit \n")
        choice = int(input("Select the operation you wish to perform (1 or 2 or 3 or 4 or 5): "))

        match choice:
            case 1:
                #addTask()
                addTask()

            case 2:
                viewTask()
            
            case 3:
                print("1. Edit task \n2. Delete task \n3. Back to menu")
                editDeleteChoice = int(input("Select the operation you wish to perform (1 or 2 or 3): "))
                match editDeleteChoice:
                    case 1:
                        editTask()
                        return menu()
                        # edit = int(input("Enter the SNo. of the task you wish to edit: "))
                        #logic
                    case 2:
                        deleteTask()
                        return menu()
                        # delete = int(input("Enter the SNo. of the task you wish to delete: "))
                        #logc
                    case 3:
                        menu()

            case 4:
                markAsDone()
                return menu()
                # done = int(input("Enter the S No. of the task you wish to mark as done: "))
                #logic

            case 5:
                break

            case _:
                print("Invalid operation selected, please select an operation between (1 or 2 or 3 or 4 or 5).")

# menu()
print(dataframe)