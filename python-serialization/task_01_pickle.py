#!/usr/bin/python3

import pickle


class CustomObject:

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            return pickle.dump(self, file)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
