import os
import sys
import datetime

# help function
def help():
    sa = """
        $ ./todo add_items "todo item" # Add a new todo
        $ ./todo list_items               # Show remaining todos
        $ ./todo del NUMBER       # Delete a todo
        $ ./todo done NUMBER      # Complete a todo
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