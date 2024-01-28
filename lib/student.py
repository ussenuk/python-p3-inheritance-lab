#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, add_knowledge):
        self.knowledge.append(add_knowledge)
        return self.knowledge

Ussen = Student("Ussen", "Kimanuka")
print(Ussen.learn("React"))