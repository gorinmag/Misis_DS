class Stack:
    def __init__(self):
        # Инициализация стека с пустым списком для хранения элементов
        self.items = []

    def push(self, item):
        # Метод для добавления элемента в стек
        self.items.append(item)

    def pop(self):
        # Метод для удаления верхнего элемента из стека
        # Если стек пуст, выбрасывает исключение
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def is_empty(self):
        # Метод для проверки, пуст ли стек
        return len(self.items) == 0

    def peek(self):
        # Метод для получения верхнего элемента стека без его удаления
        # Если стек пуст, выбрасывает исключение
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")

    def size(self):
        # Метод для получения текущего количества элементов в стеке
        return len(self.items)


class TaskManager:
    def __init__(self):
        # Инициализация менеджера задач с пустым стеком и словарем для хранения задач
        self.stack = Stack()
        self.tasks = {}

    def new_task(self, task: str, priority: int):
        # Метод для добавления новой задачи с заданным приоритетом
        # Проверяем, существует ли уже список задач с таким приоритетом
        if priority not in self.tasks:
            self.tasks[priority] = []

        # Проверяем, нет ли дубликата задачи
        if task not in self.tasks[priority]:
            self.tasks[priority].append(task)  # Добавляем задачу в список
            self.stack.push((task, priority))  # Добавляем задачу в стек (для возможного использования)

    def remove_task(self, task: str):
        # Метод для удаления задачи по её названию
        for priority, tasks in self.tasks.items():
            if task in tasks:
                tasks.remove(task)  # Удаляем задачу из списка
                # Если список задач приоритетного уровня опустел, удаляем его из словаря
                if not tasks:
                    del self.tasks[priority]
                return
        print(f"Задача '{task}' не найдена.")  # Если задача не найдена, выводим сообщение

    def __str__(self):
        # Метод для строкового представления менеджера задач
        result = []
        # Сортируем приоритеты и формируем строку для каждой группы задач
        for priority in sorted(self.tasks.keys()):
            tasks_str = "; ".join(self.tasks[priority])  # Объединяем задачи с одинаковым приоритетом в одну строку
            result.append(f"{priority} {tasks_str}")  # Формируем строку вида "приоритет задача1; задача2"
        return "\n".join(result)  # Объединяем все строки в одну с переносами




# Пример использования
# Создаем экземпляр менеджера задач
manager = TaskManager()
# Добавляем несколько задач с различными приоритетами
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

# Выводим все задачи, отсортированные по приоритету
print(manager)
# Удаляем задачу "поесть"
manager.remove_task("поесть")
print("\nПосле удаления:")
# Выводим оставшиеся задачи
print(manager)

# Попробуем удалить несуществующую задачу
manager.remove_task("несуществующая задача")