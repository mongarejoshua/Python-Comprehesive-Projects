# to-do-list program 
import json

todo_list = ['Wake up at 6 am', 'Pray', 'Take breakfast', 'Take a shower', 'Go to the gym', 'Work on my school and personal projects'] 


def main():
    while True:
        print('--- TODO LIST MENU ---')
        print('1. Show your tasks.')
        print('2. Add tasks.')
        print('3. Exit')

        choice = input('Select one option from the above(i.e 1,2,3): ')
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            print('---Goodbye---')
            break

def show_tasks():
    if len(todo_list) == 0:
        print('Your todo list is empty. No tasks to show.\n')
    else:
        print('---YOUR TASK LIST---')
        for i, task in enumerate(todo_list, 1): #prints task number and the task
            print(f'{i}. {task}')
        print('\n')

def add_task():
    task = input('Enter your tasks separated by a comma(no spaces after the comma): ')
    todo_list.extend(task.split(',')) # extend() add multiple elements to a list
    
    print('Tasks added successfully!\n')


def delete():
    pass


def edit():
    pass


main()