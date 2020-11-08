"""Copy the code used in the examples above and extend it in the following ways:

Create a Name class that has the attributes firstName, surname, title and otherNames.
You will need to use a suitable data structure for other names.
Write a method in the class called formalName() that will output a name in the following format:
Mr J. S. Greenhold or Mr J. Greenhold if there are no middle names.
Use the Name class within a Person object to demonstrate composition.
Create a sub-class of Student for DistanceStudent and add the attribute currentModule.
Using this structure and any other appropriate methods, create a DistanceStudent and printout the following:
Mr J. S. Greenhold is currently studying the Advanced Programming module."""


class Person(object):

    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def personal_details(self):
        return self.name, self.address, self.age


class Tutor(Person):
    id = 0

    def __init__(self, name, address, age, salary, id):
        super().__init__(name, address, age)
        self.salary = salary
        self.id = id

    def personal_details(self):
        return super().personal_details(), self.salary, self.id


class Student(Person):

    def __init__(self, name, address, age, id):
        super().__init__(name, address, age)
        self.id = id

    def personal_details(self):
        return super().personal_details(), self.id


class Name:

    def __init__(self, first_name, surname, title, other_names=None):
        if other_names is None:
             other_names = []
        self.first_name = first_name.title()
        self.surname = surname.title()
        self.title = title.title()
        self.other_names = other_names

    def formal_name(self):
        middle_names = ""
        for name in self.other_names:
            middle_names += name[0].upper() + ". "
        return f"{self.title} {self.first_name} {middle_names}{self.surname}"


class DistanceStudent(Student):

    def __init__(self, name, address, age, id, current_module):
        super().__init__(name, address, age, id)
        self.current_module = current_module

    def personal_details(self):
        return super().personal_details(), self.current_module

    def print_current_module_details(self):
        return f"{self.name.formal_name()} is currently studying the {self.current_module} module."


# Test Data
aidan_name = Name("aidan", "curley", "mr.", ["Paul", "Joseph"])
aidan = DistanceStudent(aidan_name, "123 Hope St.", 46, "ST112", "Advanced Programming")
print(aidan.print_current_module_details())

