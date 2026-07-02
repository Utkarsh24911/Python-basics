class Employee:
    company = "HP"

    def get_salary(self):
        print(self)
        return 34000

e=Employee()
print(e.get_salary())


e2=Employee()
print(e2.get_salary())
print(e2.company)
print(e.company)


class Animal:  
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):  
    def speak(self):
        print("Woof!")

class Cat(Animal):  
    def speak(self):
        print("Meow!")

# Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")

# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name) 
print(my_cat.name)  

# They both have a 'speak' method, but it behaves differently:
my_dog.speak()  
my_cat.speak()  


class Dog:
    def __init__(self, name, breed):
        # 'self' = reference to this object
        self.name = name
        self.breed = breed
        
    def bark(self):
        return f"{self.name}: Woof!"

# Creating specific instances
rex = Dog("Rex", "Husky")
buddy = Dog("Buddy", "Lab")

print(rex.bark())  
print(buddy.bark())  


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # __ prefix makes it private

    # Getter method to access private data safely
    def get_balance(self):
        return self.__balance

    # Setter method to modify private data with verification
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

# Using the Encapsulated Class
acct = BankAccount(1000)
print(acct.get_balance()) 

acct.deposit(500)
print(acct.get_balance()) 


class Vehicle:  # Parent class
    def __init__(self, brand):
        self.brand = brand
        
    def move(self):
        return f"{self.brand} moves"

class Car(Vehicle):  # Car IS-A Vehicle (Child class)
    def __init__(self, brand, doors):
        super().__init__(brand)  # Inherit brand initialization from parent
        self.doors = doors

# Using the Inherited Class
car = Car("Toyota", 4)
print(car.move())  
print(car.doors)    


class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):  # Overriding parent method
        return "Woof!"

class Cat(Animal):
    def sound(self):  # Overriding parent method
        return "Meow!"

# One interface — many behaviors
for animal in [Dog(), Cat()]:
    print(animal.sound())
# Output:
# Woof!
# Meow!


from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        # Contract: Any child class MUST implement this method
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):  # Implementing the abstract contract method
        return 3.14 * self.r ** 2

# Using Abstract Implementation
c = Circle(5)
print(c.area())  



class MyClass:
    className = "MyClass"
    def sayHello(self , name):
        print(f"Hello , {name}! , I am {self.className}.")

obj = MyClass()
obj.sayHello("Utkarsh") 

class Calculator:
    def add(self,x,y):
        return x+y
    
    def substract(self,x,y):
        return x-y
    
    def multiply(self,x,y):
            return x*y
        
    
    def divide(self,x,y):
        if y != 0:
            return x/y
        else:
             return "Cannot divide by zero"
        
        calc = Calculator()

        print(calc.add(5,3))
        print(calc.substract(5,3))
        print(calc.multiply(5,3))
        print(calc.divide(5,0))



class Student:
    def __init__(self, name, grade, admissionNumber):
        self.name = name
        self.grade = grade
        self.admissionNumber = admissionNumber

    def is_passing(self):
        return self.grade >= 60

    def details(self):
        return f"{self.name} (Admission Number: {self.admissionNumber}) has a grade of {self.grade}"

student1 = Student("Utkarsh", 0, "2021BTCS068")
student2 = Student("Alice", 85, "2021BTCS107")
print(student1.details())
print(student2.is_passing())

print(student1.details())
print(student2.details())


class encapsulationDemo:
    # The constructor initialized with a default or passed value
    def __init__(self, initial_value):
        # We use the setter here to ensure the initial value is also validated
        self.__private_value = 0
        self.set_value(initial_value)

    # Getter method
    def get_value(self):
        return self.__private_value

    # Setter method with validation logic
    def set_value(self, new_value):
        if new_value >= 0:
            self.__private_value = new_value
        else:
            print("Error: Value cannot be negative!")

# Creating the object and passing 10 to __init__
demo = encapsulationDemo(10)
print(demo.get_value()) 

# Updating the value using the setter
demo.set_value(20)
print(demo.get_value())  

class BankAccount:
    def __init__(self,account_number , balance=0):
        self.account_number = account_number
        #to do name mangling , in order to make it private

        self._balance = balance
    def deposit (self,amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited{amount}. New balance: {self._balace}")

        else:
            print("Deposit amount must be positive.")

    def show_balance(self):
        print(f"Account Number : {self.account_number}, Balance:{self.__balance}")
        


# from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"
    
toyota = Car()
print(toyota.start_engine())  # Car engine started
honda = Bike()
print(honda.start_engine())   # Bike engine started
    
