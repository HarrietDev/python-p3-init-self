#!/usr/bin/env python3

class Dog:
    def __init__(self,name, breed="Mutt"):
        self.name = name
        self.breed = breed

dog1 = Dog("snoopy", "german-shepherd")
print(dog1.name)
print(dog1.breed)
