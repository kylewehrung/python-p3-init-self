#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

ham_dog = Dog("Hamdog", "Ham")
print(ham_dog.name)
print(ham_dog.breed)




