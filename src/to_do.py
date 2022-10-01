import json

def create_task(name, due_date, notes):
    with open("list.json") as file:
        tasks = json.load(file)

    if name in tasks:
        print("There is already a task with this name.")
        while True:
            yn = input("Overwrite? (y/n)\n").lower()
            if yn == "y":
                break
            elif yn == "n":
                return
    tasks[name] = {"name": name, "due_date": due_date, "notes": notes}
    with open("list.json", "w") as file:
        json.dump(tasks, file)


def print_tasks():
    with open("list.json", "r") as file:
        print("".join(item.ljust(20, " ") for item in ("Task", "Due Date", "Notes")))
        tasks = json.load(file)
        for task in tasks.values():
            print("".join(field.ljust(20, " ") for field in task))


def delete_task(name):
    with open("list.json", "r") as file:
        tasks = json.load(file)
        task = tasks.pop(name)
        if task:
            print(f"Task {name} was deleted!")
        else:
            raise ValueError(f"Task {name} was not found.")

    with open("list.json", "r") as file:
        json.dump(tasks, file)
