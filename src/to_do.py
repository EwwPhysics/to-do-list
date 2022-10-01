import json

def create_task(name, due_date, notes):
    with open("list.json", "r+") as file:
        try:
            tasks = json.load(file)
        except json.decoder.JSONDecodeError:
            file.seek(0)
            file.write("{}")
            tasks = json.load(file)
        tasks[name] = {"name": name, "due_date": due_date, "notes": notes}
        file.seek(0)
        json.dump(tasks, fp=file)


def print_tasks():
    with open("list.json", "r") as file:
        print("".join(item.ljust(20, " ") for item in ("Task", "Due Date", "Notes")))
        try:
            tasks = json.load(file)
            for task in tasks:
                print("".join(tasks[task][item].ljust(20, " ") for item in tasks[task]))
        except json.decoder.JSONDecodeError:
            print("")


def delete_task(name):
    with open("list.json", "r+") as file:
        try:
            tasks = json.load(file)
            task = tasks.pop(name)
            if task:
                print(f"Task {name} was deleted!")
            else:
                raise ValueError(f"Task {name} was not found.")
            file.seek(0)
            json.dump(tasks, fp=file)
        except json.decoder.JSONDecodeError:
            print("Attempted to delete task from empty list.")
