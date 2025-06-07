Task=[]

def add_task():
    add=input("Enter the task to be added:")
    if add:
        Task.append(add)
        print("Task added!!!!!!")
    else:
        print("Task is not entered.")
def view_task():
    if not Task:
        print("No task is added yet!!!")
    
    else:
        print("Your Task:")
        for index,tasks in enumerate(Task, 1):
                print(f"{index}. {tasks}")

def remove_task():
    view_task()
    remove=int(input("Enter the task no to remove:"))
    if 0<=remove<=len(Task):
            Task.pop(remove-1)
            print("The task have been removed.")
    else:
            print("Please enter valid.")


while True:
    print("\n-- The To-Do List --")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice=int(input("Enter your choice(1/2/3/4):"))
    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        remove_task()
    elif choice==4:
        print("Task saved.Goodbye!!!!!!!!")
        break
    else:
        print("Please provide valid input!!!")