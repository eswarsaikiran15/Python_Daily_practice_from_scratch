#parent class
class Parent:
    def work(self):
        print("Parent Work")

#child class
class Child(Parent):
    def study(self):
        print("Child study")

# usage  
p=Parent()
p.work()

d=Child()
d.study()
d.work()