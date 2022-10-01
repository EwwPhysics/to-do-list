from . import to_do
import argparse

# name = input("Enter the name of the task.\n")
# due_date = input("What day is it due? Format YYYY/MM/DD\n")
# notes = input("Notes:\n")

parser = argparse.ArgumentParser()
parser.add_argument("action", default="print", help='Must be "delete", "create", or "print"')
parser.add_argument("name", nargs="?", default="")
parser.add_argument("date", nargs="?", default="")
parser.add_argument("notes", nargs="?", default="")

args = parser.parse_args()

if args.action == "delete":
    to_do.delete_task(args.name)
elif args.action == "create":
    to_do.create_task(args.name, args.date, args.notes)
elif args.action == "print":
    to_do.print_tasks()

