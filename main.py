class Task():
    def __init__(self, description, date, status):
        self.description = description
        self.date = date
        self.status = status

    def mark_task(self):
        self.status = True

def add_task():
    description = input("Введите описание задачи: ")
    date = input("Введите дату выполнения задачи: ")
    status = False
    task_id = Task(description, date, status)
    return task_id
def print_current_tasks(tasks):
    for task in tasks:
        if task.status == False:
            print(f"Описание задачи: {task.description}")
            print(f"Дата выполнения задачи: {task.date}")

# тест работы класса и функций
tasks = []
for i in range(3):
    tasks.append(add_task())

tasks[1].mark_task() # пометить вторую задачу как выполненную

print_current_tasks(tasks)