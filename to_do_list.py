
data = []
choice = 'random'

def line():
    print('-----------------------------')

def disp_menu():
    line()
    print('Reminder Menu')
    line()
    print('1. Add an item')
    print('2. Mark as done')
    print('3. View list')
    print('4. Exit')
    line()
    user_input = input('Enter your choice: ')
    return user_input

while choice != '4':
    choice = disp_menu()
    if choice == '1':
        item = input('What is to be done? ')
        data.append(item)
        print('Item', item, 'added')
    elif choice == '2':
        item = input('What is to be marked as done? ')
        if item in data:
            data.remove(item)
            print('Removed item', item)
        else:
            print('Could not find item', item)
    elif choice == '3':
        print('List of to-do items:')
        for item in data:
            print(item)
    elif choice == '4':
        print('Reminder closed')
    else:
        print('Please enter one of 1, 2, 3 or 4')
