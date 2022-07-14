import sys

# Displays usage of the app.
def app_info():
    info = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics\n"""

    print(info)


# Displays all pending items.
def list_pending():
    try:
        with open('task.txt', 'r') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            words = line.split()
            priority, task = words[0], ' '.join(words[1:])
            print(f'{i+1}. {task} [{priority}]')
    except FileNotFoundError:
        print('There are no pending tasks!')


# Adds new item to task list.
def add_item(priority, item):
    try:
        with open("task.txt", 'r') as f:
            lines = f.readlines()
            items = []
            for line in lines:
                words = line.split()
                items.append((int(words[0]), ' '.join(words[1:])))
            
        new_task = (int(priority), item)
        items.append(new_task)
        items.sort(key=lambda a: a[0])

        with open('task.txt', 'w') as f:
            for i in items:
                task = f'{i[0]} {i[1]}\n'
                f.write(task)

        print(f'Added task: "{item}" with priority {priority}')
    except FileNotFoundError:
        with open('task.txt', 'w') as f:
            task = f'{priority} {item}\n'
            f.write(task)

        print(f'Added task: "{item}" with priority {priority}')


# Deletes item from the task list.
def delete_item(index):
    index = int(index)
    try:
        with open("task.txt", 'r') as f:
            lines = f.readlines()
            items = []
            for line in lines:
                words = line.split()
                items.append((int(words[0]), ' '.join(words[1:])))
    except FileNotFoundError:
        print('There are no tasks to delete!')
    else:
        if index in range(1, len(items)+1):
            items.pop(index-1)
            with open('task.txt', 'w') as f:
                for i in items:
                    task = f'{i[0]} {i[1]}\n'
                    f.write(task)
            print(f'Deleted task #{index}')
        else:
            print(f'Error: task with index #{index} does not exist. Nothing deleted.')


# Marks item as completed.
def mark_completed(index):
    index = int(index)
    try:
        with open("task.txt", 'r') as f:
            lines = f.readlines()
            items = []
            for line in lines:
                words = line.split()
                items.append((int(words[0]), ' '.join(words[1:])))
    except FileNotFoundError:
        print('There are no pending tasks!')
    else:
        if index in range(1, len(items)+1):
            completed = items.pop(index-1)
            with open('task.txt', 'w') as f:
                for i in items:
                    task = f'{i[0]} {i[1]}\n'
                    f.write(task)

            with open('completed.txt', 'a') as f:
                f.write(f'{completed[1]}\n')
            
            print('Marked item as done.')
        else:
            print(f'Error: no incomplete item with index #{index} exists.')
    

# Displays report of pending and completed items
def report():
    try:
        with open("task.txt", 'r') as f:
            lines = f.readlines()
            pending_tasks = []
            for line in lines:
                words = line.split()
                pending_tasks.append((int(words[0]), ' '.join(words[1:])))
    except FileNotFoundError:
        print('There are no pending tasks!')
    else:
        print(f'Pending : {len(pending_tasks)}')
        for i, task in enumerate(pending_tasks):
            print(f'{i+1}. {task[1]} [{task[0]}]')

    try:
        with open("completed.txt", 'r') as f:
            lines = f.readlines()
            completed_tasks = []
            for line in lines:
                line = line.strip()
                completed_tasks.append(line)
    except FileNotFoundError:
        print('There are no completed tasks!')
    else:
        print(f'\nCompleted : {len(completed_tasks)}')
        for i, task in enumerate(completed_tasks):
            print(f'{i+1}. {task}')


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        cmd = args[1]
    else:
        cmd = ''

    if cmd == '' or cmd == 'help':
        if len(args) > 2:
            print('Error: Missing tasks string. Nothing added!')
        else:
            app_info()
    elif cmd == 'ls':
        if len(args) > 2:
            print('Incorrect command. Please enter help command to see usage.')
        else:
            list_pending()
    elif cmd == 'add':
        if len(args) != 4:
            print('Error: Missing tasks string. Nothing added!')
        else:
            if int(args[2]) < 0:
                print('Priority must be >= 0')
            else:
                add_item(args[2], args[3])
    elif cmd == 'del':
        if len(args) != 3:
            print('Error: Missing NUMBER for deleting tasks.')
        else:
            delete_item(args[2])
    elif cmd == 'done':
        if len(args) != 3:
            print('Error: Missing NUMBER for marking tasks as done.')
        else:
            mark_completed(args[2])
    elif cmd == 'report':
        report()