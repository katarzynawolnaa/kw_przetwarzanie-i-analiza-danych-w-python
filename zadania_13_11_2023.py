# -*- coding: utf-8 -*-
"""ZADANIA-13-11-2023

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w4kUZ-YJbMqXwXxtgQH4RvzeC3vYKxkg

Zad.1
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

student1 = Student("Anna Ciozak", [60, 75, 80, 90])
student2 = Student("Michał Kowalik", [40, 30, 45, 55])

print(f"{student1.name} zdał/a: {student1.is_passed()}")
print(f"{student2.name} zdał/a: {student2.is_passed()}")

"""Zad.2"""

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\n" \
               f"Open hours: {self.open_hours}\n" \
               f"Phone: {self.phone}\n"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\n" \
               f"Hire date: {self.hire_date}\n" \
               f"Birth date: {self.birth_date}\n" \
               f"Address: {self.city}, {self.street}, {self.zip_code}\n" \
               f"Phone: {self.phone}\n"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\n" \
               f"Publication date: {self.publication_date}\n" \
               f"Number of pages: {self.number_of_pages}\n" \
               f"Belongs to Library: {self.library.city}, {self.library.street}\n"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"   - {book.author_name} {book.author_surname}" for book in self.books])
        return f"Order:\n" \
               f"Order date: {self.order_date}\n" \
               f"Employee: {self.employee.first_name} {self.employee.last_name}\n" \
               f"Student: {self.student}\n" \
               f"Books:\n{book_list}\n"


library1 = Library("City1", "Street1", "12345", "9 AM - 6 PM", "123-456-789")
library2 = Library("City2", "Street2", "54321", "10 AM - 7 PM", "987-654-321")

employee1 = Employee("John", "Doe", "2022-01-01", "1990-05-15", "City1", "Street1", "12345", "111-222-333")
employee2 = Employee("Jane", "Smith", "2022-02-01", "1985-08-20", "City2", "Street2", "54321", "444-555-666")
employee3 = Employee("Alice", "Johnson", "2022-03-01", "1995-03-10", "City1", "Street1", "12345", "777-888-999")

book1 = Book(library1, "2021-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2022-02-02", "Author2", "Surname2", 250)
book3 = Book(library2, "2020-03-03", "Author3", "Surname3", 180)
book4 = Book(library2, "2023-04-04", "Author4", "Surname4", 300)
book5 = Book(library1, "2022-05-05", "Author5", "Surname5", 220)

student1 = "Student1"
student2 = "Student2"
student3 = "Student3"

order1 = Order(employee1, student1, [book1, book2, book3], "2023-01-15")
order2 = Order(employee2, student2, [book4, book5], "2023-02-20")

print(order1)
print(order2)

"""Zad.3"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property:\n" \
               f"Area: {self.area} sq. m\n" \
               f"Rooms: {self.rooms}\n" \
               f"Price: ${self.price}\n" \
               f"Address: {self.address}\n"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f"Plot size: {self.plot} sq. m\n"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f"Floor: {self.floor}\n"


house = House(area=150, rooms=5, price=200000, address="123 Main St", plot=500)
flat = Flat(area=80, rooms=3, price=120000, address="456 Oak St", floor=2)

print(house)
print(flat)