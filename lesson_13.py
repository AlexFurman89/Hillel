# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП


class Academy:
    __academy_name: str=None
    __academy_address: str=None
    __academy_phone: str=None
    def __init__(self, academy_name: str=None, academy_address: str=None, academy_phone: str=None):
        self.set_name(academy_name)
        self.set_address(academy_address)
        self.set_phone(academy_phone)
    def set_name(self,academy_name):
        self.__academy_name=academy_name

    def get_name(self, academy_name):
        return self.__academy_name
    def set_address(self,academy_address):
        self.__academy_address=academy_address

    def get_address(self):
        return self.__academy_address

    def set_phone(self,academy_phone):
        self.__academy_phone=academy_phone
    def get_phone(self):
        return self.__academy_phone

    def show_info(self):
        print(f"Academy name: {self.__academy_name}, Academy address: {self.__academy_address}, Academy phone: {self.__academy_phone}")


class Person:

    def __init__(self, first_name=None, last_name=None):
        self.first_name=first_name
        self.last_name=last_name
    def show_info(self):
        print(f"first name: {self.first_name}, last name: {self.last_name}")

class Teacher(Person):
    def __init__(self, first_name=None, last_name=None, subject=None):
        super().__init__(first_name, last_name)
        self.subject=subject
    def show_info(self):
        print(f"Teacher name {self.first_name}, last name {self.last_name}, teacher subject {self.subject}")

class Student(Person):
    def __init__(self, first_name=None, last_name=None, university=None):
        super().__init__(first_name, last_name)
        self.university=university

    def show_info(self):
        print(f"Student_name: {self.first_name}, Student second name: {self.last_name}, stident at university: {self.university}")

academy_first=Academy("KPI","Premogy str","0441234566")
academy_first.set_phone("0449999999")
print(academy_first.get_address())


person_first=Person("Alex", "Furman")
person_first.show_info()

teacher_first=Teacher("Alex", "Furman", "Math")
teacher_first.show_info()

student_first=Student("Alex", "Furman", "KPI")
student_first.show_info()