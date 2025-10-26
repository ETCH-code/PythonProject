class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def meow(self):
        print(f"Meow! My name is {self.name} and my age is {self.age}")

my_cat = Cat("Tom", 7)
my_cat.meow()