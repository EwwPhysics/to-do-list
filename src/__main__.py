from . import to_do

# Make sure the data file exists
try:
    with open("list.json"):
        pass
except IOError:
    with open("list.json") as file:
        file.write("{}")

while True:
    choice = input("What would you like to do?")
    print("""1. Create task
2. Print tasks.
3. Delete tasks.
""")
    try:
        choice = int(choice)
    except ValueError:
        print("That wasn't a valid choice D:")
        continue

    if choice == 1:
        name = input("Enter the name of the task.\n")
        due_date = input("What day is it due? Format YYYY/MM/DD\n")
        notes = input("Notes:\n")
        to_do.create_task(name, due_date, notes)
    elif choice == 2:
        to_do.print_tasks()
    elif choice == 3:
        name = input("Enter the name of the task to delete.\n")
        to_do.delete_task(name)

