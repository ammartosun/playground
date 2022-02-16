class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("woof woof!")
    
    def fetch(self, stick):

        if stick > 10:
            self.bark()
            return False
        elif stick < 2:
            return True
        else:
            self.bark()
            self.bark()
            return True



myDog = Dog("karabas", 13)
print(myDog.age)
print(myDog.name)

# myDog.bark()
print(myDog.fetch(8))

# myDog.age = 2
# print(myDog.age)
# myDog.name = "pamuk"
# print(myDog.name)

# yourDog = myDog
# print(yourDog.age)
# print(yourDog.name)

# print(yourDog is myDog)
# print(yourDog == myDog)

# yourDog.name = 'pamuk'
# print(yourDog.name)
# print(myDog.name)

# del myDog
# print(yourDog.name)
# print(myDog.name)

# yourDog = Dog("karabas", 13)
# print(yourDog == myDog)
