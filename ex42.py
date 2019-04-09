## Animal inherits from object (implicit)
class Animal:
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
class Person:
    def __init__(self, name):
        self.name = name
        self.pet = None
    
class Employee(Person):
    def __init__(self, name, salary):
        # super(Employee, self).__init__(name) # Get name from inherited class
        super().__init__(name)
        self.salary = salary

class Fish:
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Frank is-a Employee
frank = Employee("Frank", 200)

print(frank.name, frank.salary)

## Frank has-a pet
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Couse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
