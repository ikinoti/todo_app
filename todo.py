import os
import sys
import datetime

# help function
def help():
    sa = """
        $ ./todo add_items "todo item" # Add a new todo
        $ ./todo list_items               # Show remaining todos
        $ ./todo del NUMBER       # Delete a todo
        $ ./todo complete_task NUMBER      # Complete a todo
        $ ./todo help             # Show usage
        $ ./todo report           # Statistics
    """
    sys.stdout.buffer.write(sa.encode('utf8'))


# Function to add items
def add_items(s):
    file = open('todo.txt', 'a')
    file.write(s)
    file.write('\n')
    file.close()
    s = '"'+s+'"'
    print(f'Added todo: {s}')

# Function to print items in the todo list
def list_items():
    try:
        nec()
        l = len(d)
        k = l

        for i in d:
            sys.stdout.buffer.write(f'[{l}] {d[l]}'.encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l - 1
    except Exception as e:
        raise e

# function to complete a todo   
def complete_task(num):
    try:
        nec()
        num = int(num)
        file = open('done.txt', 'a')
        st = 'x '+str(datetime.datetime.today()).split()[0]+' '+d[num]

        file.write(st)
        file.write("\n")
        file.close()
        print(f'Marked todo #{num} as done.')

        with open("todo.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)

            for i in lines:
                if i.strip('\n') != d[num]:
                    file.write(i)
                file.truncate()
    except:
        print(f'Error: todo #{num} does not exist.')

# Function to show report/statistics of todo list
def report():
    nec()
    try:
        completed_task = open('done.txt', 'r')
        counter = 1

        for line in completed_task:
            line = line.strip('\n')
            don.update({counter: line})
            counter = counter + 1

            print(f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')
            
    except:
        print(f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')

# function to delete an item from todo list
def del_item(num):
    try:
        num = int(num)
        nec()

        # utility function defined in main
        with open("todo.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)

            for i in lines:
                if i.strip('\n') != d[num]:
                    file.write(i)
            file.truncate()
        print(f"Deleted todo #{num}")

    except Exception as e:
        print(f'Error: todo #{num} does not exist. Nothing deleted.')
