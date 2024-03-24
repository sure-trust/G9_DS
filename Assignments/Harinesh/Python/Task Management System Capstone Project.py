class Task:
    def __init__(self, task_id, name, description, priority):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.priority = priority

    def display_task_details(self):
        print(f"Task ID: {self.task_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Priority: {self.priority}")
        

class TaskManagementSystem:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self):
        name=str(input("Enter task name: "))
        description=str(input("Enter task description: "))
        priority=int(input("Enter task priority: "))
        
        task = Task(self.task_id_counter, name, description, priority)
        self.tasks.append(task)
        self.task_id_counter += 1
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            for task in self.tasks:
                task.display_task_details()
        else:
            print("No tasks found.")

    def update_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                name = input("Enter new task name: ")
                description = input("Enter new task description: ")
                priority = int(input("Enter new task priority: "))
                
                task.name = name
                task.description = description
                task.priority = priority
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found.")

    def save_tasks_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.task_id},{task.name},{task.description},{task.priority}\n")

    def load_tasks_from_file(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task_id, name, description, priority = line.strip().split(',')
                    task = Task(int(task_id), name, description, int(priority))
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No saved tasks found.")

# Main Program
task_manager = TaskManagementSystem()

while True:
    print("\nTask Management System Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_manager.add_task()
    elif choice == "2":
        task_manager.view_tasks()
    elif choice == "3":
        task_id = int(input("Enter task ID to update: "))
        task_manager.update_task(task_id)
    elif choice == "4":
        task_id = int(input("Enter task ID to delete: "))
        task_manager.delete_task(task_id)
    elif choice == "5":
        task_manager.save_tasks_to_file()
    elif choice == "6":
        task_manager.load_tasks_from_file()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
