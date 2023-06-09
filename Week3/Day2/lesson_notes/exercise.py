class Employee:
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary

    def get_fullname(self):
       return self.firstname + self.lastname
    
    def happy_birthday(self):
        self.age += 1
        return self.age

    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount

    def __gt__(self, other_user):
        if self.salary > other_user.salary:
            return self.firstname
        else:
            return other_user.firstname
        
        #return self.name if self.salary > other_user.salary else other_user.firstname
        
    def __add__(self, other_user):
        return self.salary + other_user.salary
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.age} years old {self.job} {self.salary}"

user1 = Employee("Lea", "Smith", 30, "developer", 30000)
user2 = Employee("David", "Schartz", 20, "project manager", 20000)

user1.get_fullname()
user1.happy_birthday()
user1.get_promotion(500)

user2.get_fullname()
user2.happy_birthday()
user2.get_promotion(1500)

print(f"{user1.firstname} {user1.lastname} {user1.age} years old {user1.job} {user1.salary}")
print(f"{user2.firstname} {user2.lastname} {user2.age} years old {user2.job} {user2.salary}")



# реализовать метод gt dunder, который получает 2 разных сотрудников и возвращает сотрудника с самой высокой зарплатой
# реализовать метод add dunder, который получает 2 разных сотрудников и возвращает общую зарплату 2 сотрудников.
# реализовать метод str dunder, который представляет сотрудника
# Вызвать все методы
print(user1 > user2)
print(user1 + user2)
print(user1)



class Developer(Employee):

    def __init__(self, firstname, lastname, age, job = "developer", salary = 15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.codding_skills = []

    def add_skills(self, *skills):
        for skill in skills:
            #добавляем все скиллы по очереди
            self.codding_skills.append(skill)
        return self.codding_skills
    
    def coding(self):
        all_skills = ', '.join(self.codding_skills)
        sentence = f"{self.firstname} knows {all_skills} languages"
        return sentence

    def coding_with_partner(self, other_developer):
        print(f"{self.coding()} - {other_developer.coding()}")

dev1 = Developer("Tom", "Cruiz", 30)
print(f"{dev1.firstname} {dev1.lastname} {dev1.age} years old")
dev2 = Developer("Angelina", "Jolie", 23)
print(f"{dev2.firstname} {dev2.lastname} {dev2.age} years old")
dev1.add_skills("Dev", "Javascript", "Python")
dev2.add_skills("PHP", "Ruby")
dev1.coding_with_partner(dev2)






#module
# from name_file import methods
# from random import choice

import random

def game():
    lst_names = ["John", "Lea", "Emma", "Josh", "Eli"]
    lst_lastnames = ["Cohen", "Smith", "Doe", "Sevi", "Swatz"]
    lst_jobs = ["developer", "dancer", "cowboy", "tennis player", "doctor"]
    all_employees = []
    
    for i in range(10):
        random_name = random.choice(lst_names)
        random_lastname = random.choice(lst_lastnames)
        random_job = random.choice(lst_jobs)
        random_age = random.randint(18, 65)
        random_salary = random.randint(10000, 40000)

#создаем новых 10 случайных эмплои
        new_employee = Employee(random_name, random_lastname, random_age, random_job, random_salary)
        print(new_employee.__dict__)
        all_employees.append(new_employee)
        print(all_employees) #list with 10 objects
        print(all_employees[0].get_fullname())
    
print(random.choice(lst_names))
print(random.choice(lst_lastnames))
print(random.choice(lst_jobs))
print(random.randint(18, 65))
print(random.randint(10000, 40000))

game()


