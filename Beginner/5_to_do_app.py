import json

tasks = []

def main():
    while True:
        print('--- TODO LIST MENU ---')
        print('1. Add tasks')
        print('2. Show your tasks')
        print('3. Exit')

        choice = input('Select one option from the above(i.e 1,2,3): ')
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            save_task()
            break

def load_tasks():
    global tasks
    try:
        with open("task_list.json", "r") as file:
            tasks = json.load(file)
        print("Tasks Loaded successfully")
    except FileNotFoundError:
        print(f"The file {file} is not available")
        
        
def show_tasks():
    if not tasks:
        print("Task list is empty.")
    else:
        for task in tasks:
            print(task)
            

def add_task():
    task = input('Enter your tasks separated by a comma(no spaces after the comma): ')
    tasks.extend(task.split(',')) # extend() add multiple elements to a list
    save_task()
    print('Tasks added and saved successfully!\n')

def save_task():
    with open("task_list.json", "w") as file:
        json.dump(tasks, file, indent=4)
    
    

def delete():
    pass


def edit():
    pass


if __name__ == "__main__":
    load_tasks()
    main()