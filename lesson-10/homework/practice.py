# ============================================================
#   COMBINED HOMEWORK PROJECTS
#   1. ToDo List Application
#   2. Simple Blog System
#   3. Simple Banking System
# ============================================================


# -------------------------------
# Homework 1: ToDo List
# -------------------------------
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅ Completed" if self.completed else "❌ Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{title}' marked as complete!")
                return
        print("Task not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        incomplete = [t for t in self.tasks if not t.completed]
        if not incomplete:
            print("No incomplete tasks.")
            return
        for task in incomplete:
            print(task)


def todo_cli():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Show Incomplete Tasks")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Task title: ")
            description = input("Task description: ")
            due_date = input("Due date: ")
            todo.add_task(Task(title, description, due_date))
            print("Task added!")
        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            todo.mark_task_complete(title)
        elif choice == "3":
            todo.list_all_tasks()
        elif choice == "4":
            todo.list_incomplete_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


# -------------------------------
# Homework 2: Simple Blog System
# -------------------------------
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully!")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for post in self.posts:
            print(post)

    def list_posts_by_author(self, author):
        filtered = [p for p in self.posts if p.author.lower() == author.lower()]
        if not filtered:
            print("No posts by this author.")
            return
        for post in filtered:
            print(post)

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' deleted.")
                return
        print("Post not found.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title.lower() == title.lower():
                post.content = new_content
                print("Post updated!")
                return
        print("Post not found.")

    def latest_posts(self, count=3):
        latest = self.posts[-count:]
        for post in reversed(latest):
            print(post)


def blog_cli():
    blog = Blog()
    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Edit Post")
        print("5. Delete Post")
        print("6. Show Latest Posts")
        print("7. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == "2":
            blog.list_all_posts()
        elif choice == "3":
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)
        elif choice == "4":
            title = input("Enter post title to edit: ")
            new_content = input("Enter new content: ")
            blog.edit_post(title, new_content)
        elif choice == "5":
            title = input("Enter post title to delete: ")
            blog.delete_post(title)
        elif choice == "6":
            blog.latest_posts()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")


# -------------------------------
# Homework 3: Simple Banking System
# -------------------------------
class Account:
    def __init__(self, acc_number, holder_name, balance=0.0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Overdraft not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account Number: {self.acc_number}\nHolder: {self.holder_name}\nBalance: ${self.balance:.2f}\n"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Account added successfully!")

    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def check_balance(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(f"Balance for {acc.holder_name}: ${acc.balance:.2f}")
        else:
            print("Account not found.")

    def deposit_money(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_money(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found.")

    def transfer_money(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if not sender or not receiver:
            print("Invalid account number(s).")
            return
        if sender.balance < amount:
            print("Transfer failed: Insufficient funds.")
            return
        sender.withdraw(amount)
        receiver.deposit(amount)
        print(f"Transferred ${amount:.2f} from {sender.holder_name} to {receiver.holder_name}.")

    def display_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        for acc in self.accounts:
            print(acc)


def bank_cli():
    bank = Bank()
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display All Accounts")
        print("7. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            num = input("Account Number: ")
            name = input("Holder Name: ")
            balance = float(input("Initial Balance: "))
            bank.add_account(Account(num, name, balance))
        elif choice == "2":
            num = input("Account Number: ")
            bank.check_balance(num)
        elif choice == "3":
            num = input("Account Number: ")
            amt = float(input("Amount to deposit: "))
            bank.deposit_money(num, amt)
        elif choice == "4":
            num = input("Account Number: ")
            amt = float(input("Amount to withdraw: "))
            bank.withdraw_money(num, amt)
        elif choice == "5":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amt = float(input("Amount to transfer: "))
            bank.transfer_money(from_acc, to_acc, amt)
        elif choice == "6":
            bank.display_accounts()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")


# -------------------------------
# MAIN MENU (Combined)
# -------------------------------
def main_menu():
    while True:
        print("\n===============================")
        print("  MAIN MENU - Homework Projects")
        print("===============================")
        print("1. ToDo List Application")
        print("2. Simple Blog System")
        print("3. Simple Banking System")
        print("4. Exit")

        choice = input("Select a project: ")
        if choice == "1":
            todo_cli()
        elif choice == "2":
            blog_cli()
        elif choice == "3":
            bank_cli()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the combined program
if __name__ == "__main__":
    main_menu()
