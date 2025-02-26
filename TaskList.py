
# Define a function to add tasks to the list
def add_task(task_list, task):
    task_list.append(task)
    

# Define a function to display tasks
def display_tasks(task_list):
    if not task_list:
        print("No tasks to show.")
    else:
        print("Tasks:")
        for idx, task in enumerate(task_list, 1):
            print(f"{idx}. {task}")

            # Main program
tasks = []  # Initialize an empty list to store tasks

while True:
   
        #'new_task = input("Enter the task: ")
        add_task(tasks, "Add Water")
        add_task(tasks, "Feed the cat")
        add_task(tasks, "Buy groceries")
        add_task(tasks, "Pay bills")
        add_task(tasks, "Cook dinner")
        display_tasks(tasks)
        #sort the list
        tasks.sort()
        break
display_tasks(tasks)
# remove the task
tasks.remove("Buy groceries")
display_tasks(tasks)

#edit a Task
tasks[2] = "Buy milk"   
display_tasks(tasks)





    
    
    
# Call the function to add tasks to the list    