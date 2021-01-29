HELP = """ Available commands:
help - ask for help
add - add task to list
print - print tasks from list"""

tasks = ["Убраться дома"]

print(HELP)


while True:

    command = input("Введите команду: ")
    command = command.strip().lower()
    if command == "help":
        print(HELP)
    elif command == "add":
        task = input("ВВедите задачу: ")
        tasks.append(task)
    elif command == "print":
        print(tasks)
    else:
        print("Неизвестная команда")
        break
