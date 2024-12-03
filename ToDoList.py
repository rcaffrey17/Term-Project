class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        return f"Task: {self.name}, Priority: {self.priority}, Due: {self.due_date}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority, due_date):
        new_task = Task(name, priority, due_date)
        self.tasks.append(new_task)
        print(f"Task '{name}' added successfully.")

    def remove_task(self, name):
        task_found = False
        for task in self.tasks:
            if task.name.lower() == name.lower():
                self.tasks.remove(task)
                print(f"Task '{name}' removed successfully.")
                task_found = True
                break
        if not task_found:
            print(f"Error: Task '{name}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def prioritize_tasks(self):
        self.tasks.sort(key=lambda task: task.priority)
        print("Tasks sorted by priority.")

def validate_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt)
        if valid_options and user_input.lower() not in valid_options:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")
        else:
            return user_input

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Manager:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Tasks")
        print("5. Exit")
        
        choice = validate_input("Choose an option (1-5): ", valid_options=["1", "2", "3", "4", "5"])

        if choice == "1":
            name = input("Enter task name: ")
            priority = int(input("Enter task priority (1 = high, 5 = low): "))
            due_date = input("Enter task due date (e.g., YYYY-MM-DD): ")
            todo_list.add_task(name, priority, due_date)

        elif choice == "2":
            name = input("Enter task name to remove: ")
            todo_list.remove_task(name)

        elif choice == "3":
            todo_list.list_tasks()

        elif choice == "4":
            todo_list.prioritize_tasks()

        elif choice == "5":
            print("Exiting To-Do List Manager.")
            break

if __name__ == "__main__":
    main()
