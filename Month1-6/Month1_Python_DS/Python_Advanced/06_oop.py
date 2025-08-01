# Task 1 & 3: Person class with encapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name    # Encapsulated attribute
        self.__age = age      # Encapsulated attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")

    # Polymorphic method
    def introduce(self):
        print(f"Hello, my name is {self.__name} and I am {self.__age} years old.")


# Task 2: Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.__roll_no = roll_no    # Encapsulated attribute

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    # Polymorphic method (overrides Person)
    def introduce(self):
        print(f"Hi, I am {self.get_name()}, a student. My roll number is {self.__roll_no}.")


# Task 4: Teacher class with polymorphism
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject    # Encapsulated attribute

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject

    # Polymorphic method (overrides Person)
    def introduce(self):
        print(f"Hi, I am {self.get_name()}, a teacher. I teach {self.__subject}.")


# --- Demonstration of Polymorphism ---
people = [
    Person("Maroof", 17),
    Student("Maroof", 17, 123),
    Teacher("Maroof", 30, "Math")
]

for person in people:
    person.introduce()
