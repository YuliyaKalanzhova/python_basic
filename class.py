class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"The dog with name {self.name} is sitting")

    def roll_over(self):
        print(f"The dog with name {self.name} is rolling over")

my_dog = Dog("Barsik", 2)
print(f"My dog`s name is {my_dog.name}")
print(f"My dog`s age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Daby", 3)
your_dog.sit()
your_dog.roll_over()

#change:
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"the dog with name {self.name} is sitting")

    def roll_over(self):
        print(f"The dog with name {self.name} is rolling over")

    def setName(self, upd_name):
        self.name = upd_name

    def setAge(self, upd_age):
        self.age = upd_age

fourth_dog = Dog("Carl", 4)
fourth_dog.sit()
fourth_dog.roll_over()

print()

fourth_dog.setName("Harry")
fourth_dog.setAge(5)

fourth_dog.sit()
fourth_dog.roll_over()