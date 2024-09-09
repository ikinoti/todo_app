# import os
import sys
import datetime

# help function
def help():
    sa = """
        $ ./todo add_items "todo item" # Add a new todo
        $ ./todo list_items               # Show remaining todos
        $ ./todo del_item NUMBER       # Delete a todo
        $ ./todo complete_task NUMBER      # Complete a todo
        $ ./todo help             # Show usage
        $ ./todo report           # Statistics
    """
    sys.stdout.buffer.write(sa.encode('utf8'))


# Function to add todo items
def add_items(todo_item):
    file = open('todo.txt', 'a')
    file.write(todo_item)
    file.write('\n')
    file.close()
    todo_item = '"'+todo_item+'"'
    print(f'Added todo: {todo_item}')

# Function to print items in the todo list
def list_items():
    try:
        nec()
        list_len = len(d)
        k = list_len

        for i in d:
            sys.stdout.buffer.write(f'[{list_len}] {d[list_len]}'.encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            list_len = list_len - 1
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

# utility function
def nec():

    # utility function used in complete_task and report function
    try:
        file = open('todo.txt', 'r')
        counter = 1
        for line in file:
            line = line.strip('\n')
            d.update({counter: line})
            counter += 1
    except:
        sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))


# main
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv

        if(args[1] == 'del_item'):
            args[1] = 'del_item'

        if(args[1] == 'add_items' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Missing todo string. Nothing added!".encode('utf8'))
        elif(args[1] == 'complete_task' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Missing NUMBER for marking todo as done.".encode('utf8'))
        elif(args[1] == 'del_item' and len(args[2:]) == 0):
            sys.stdout.buffer.write("Error: Missing NUMBER for deleting todo.".encode('utf8'))
        else:
            globals()[args[1]](*args[2:])
    except Exception as e:
        s = """
            Usage :-
                $ ./todo add_items "todo item" # Add a new todo
                $ ./todo list_items            # Show remaining todos
                $ ./todo del_item NUMBER       # Delete a todo
                $ ./todo complete_task NUMBER  # Complete a todo
                $ ./todo help                  # Show usage
                $ ./todo report                # Statistics 

            """
        sys.stdout.buffer.write(s.encode('utf8'))