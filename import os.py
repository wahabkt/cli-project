import os

FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from file into a list."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    """Save the list of tasks to file."""
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    """Display the current tasks."""
    if not tasks:
        print("\n✅ No tasks yet.")
        return
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added.")
    else:
        print("⚠️ Task cannot be empty.")

def delete_task(tasks):
    """Delete a task by number."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑️ Removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    """Main program loop."""
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO CLI ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
