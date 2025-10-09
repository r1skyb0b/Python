# ===============================
# 1. Circle Class
# ===============================
import math
from datetime import date

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# ===============================
# 2. Person Class
# ===============================
class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date  # format: YYYY-MM-DD

    def age(self):
        birth_year, birth_month, birth_day = map(int, self.birth_date.split('-'))
        today = date.today()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        return age


# ===============================
# 3. Calculator Class
# ===============================
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# ===============================
# 4. Shape and Subclasses
# ===============================
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# ===============================
# 5. Binary Search Tree Class
# ===============================
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left:
                self._insert(root.left, key)
            else:
                root.left = Node(key)
        elif key > root.key:
            if root.right:
                self._insert(root.right, key)
            else:
                root.right = Node(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)


# ===============================
# 6. Stack Data Structure
# ===============================
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return "Stack is empty"
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# ===============================
# 7. Linked List Data Structure
# ===============================
class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = NodeLL(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ===============================
# 8. Shopping Cart Class
# ===============================
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())


# ===============================
# 9. Stack with Display
# ===============================
class DisplayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print("Stack contents:", self.stack)


# ===============================
# 10. Queue Data Structure
# ===============================
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def display(self):
        print("Queue contents:", self.queue)


# ===============================
# 11. Bank Class
# ===============================
class Account:
    def __init__(self, acc_number, name, balance=0):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount

    def __str__(self):
        return f"{self.name} - Balance: ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc_number, name, balance=0):
        self.accounts[acc_number] = Account(acc_number, name, balance)

    def deposit(self, acc_number, amount):
        if acc_number in self.accounts:
            self.accounts[acc_number].deposit(amount)

    def withdraw(self, acc_number, amount):
        if acc_number in self.accounts:
            print(self.accounts[acc_number].withdraw(amount))

    def show_accounts(self):
        for acc in self.accounts.values():
            print(acc)


# ===============================
# Sample Testing (optional)
# ===============================
if __name__ == "__main__":
    # Circle Test
    c = Circle(5)
    print("Circle area:", c.area())
    print("Circle perimeter:", c.perimeter())

    # Person Test
    p = Person("Alice", "USA", "1990-05-12")
    print("Age:", p.age())

    # Calculator Test
    calc = Calculator()
    print("Add:", calc.add(5, 3))

    # Bank Test
    b = Bank()
    b.add_account(1, "John", 500)
    b.deposit(1, 200)
    b.withdraw(1, 100)
    b.show_accounts()
