# Task N1

HELP = """ Available commands:
help - ask for help
add - add task to list
print - print tasks from list
exit - exit from program """

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
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break
