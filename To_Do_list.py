
user_choice = -1

tasks = []
tasks.append("Tidy room")

def show_tasks():
    task_index = 0
    for task in tasks:
        print("[" + str(task_index) + "] " + task )
        task_index +=1

def add_task():
    task = input("Write task's content: ")
    tasks.append(task)
    print("Task added succesfully!")

def delete_task():
    task_index = int(input("Choose number of task: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("Exercise of this numer don't exist!")

    tasks.pop(task_index)
    print("Task deleted succesfully!")

while user_choice != 5:

    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()
        

    if user_choice == 3:
        delete_task()

    print()
    print("------ To Do List ------ \n")

    print("1.Show tasks.")
    print("2.Add task.")
    print("3.Delete task.")
    print("4.Save tasks to the file.")
    print("5.Exit.")

    user_choice = int(input("Choose operation: "))
    print()


