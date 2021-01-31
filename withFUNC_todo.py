HELP = """ Available commands:
* todo - add task to list
* help - ask for help
* print - print tasks from list
* exit - exit from program """

print(HELP)

todos = dict()  # todos = {}


def add_todo(date, task):
    if date in todos:
        todos[date].append(task)
    else:
        todos[date] = [task]
    print(f"Задача {task} добавлена на дату {date}")


stop = False
while not stop:

    command = input("Введите команду: \n")
    command = command.strip().lower()
    if command == "help":
        print(HELP)
    elif command == "todo":
        date = input("Введите дату: ")
        task = input("Введите задачу: ")
        # <----------------->
        add_todo(date, task)
    elif command == "print":
        date = input("Введите дату: ")
        if date in todos:
            print(date)
            for i in todos[date]:
                # print(f"{i}")  # this works, prints without [], only items
                print("[] ", i)  # this works too
            # print(todos[date]) # just to control everything is fine
        else:
            print(f"Задач на дату {date} нет")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        stop = True
    else:
        print("Неизвестная команда")
        stop = True
