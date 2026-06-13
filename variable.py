age = 34 #integer
name = "utkarsh" #string
cgpa = 9.8 #float
is_completed = True #boolean
print(age)
print(type(age))
print(name)
print(type(name))
print(cgpa)
print(type(cgpa))
print(is_completed)
print(type(is_completed))


# TYPECASTING

a=35
b="35"
d=55.5
print(a)
print(type(a))

print(b)
print(type(b))

c= int(b)
print(c)
print(type(c))

e=str(d)
print(e)
print(type(e))

# TAKING USER INPUT

a= input("Enter a number:")
b= input("Enter a name:")
print(a)
print(b)

a=int(input("Enter first number:"))
# a=int(a)
b=int(input("Enter second number:"))
# b=int(b)
print(a+b)


# ESCAPE SEQUENCE CHARACTER 

print("hello\nmy name is \''kumar utkarsh\'' i\t     lives in \'ranchi\' it is a beautiful place")

print('Hello world' , "vasu" , 5 , sep=";")
print("hello world", end='.')
print('\nvasu', end=">>")

# OPERATORS

# 1) Arithmetic operators

a=29
b=12

print("we get a+b=", a+b)
print("we get a-b=", a-b)
print("we get a*b=", a*b)
print("we get a/b=", a/b)
print("we get a%b=", a%b)
print("we get a//b=", a//b)
print("we get a**b=", a**b)

# 2) Comparision Operators


a=22
print(a>5)
print(a<5)
print(a>=5)
print(a<=5)
print(a==5)
print(a==22)
print(a!=5)

# 3)Logical operators

print("\nand operator\n")
print (True and True)
print (True and False)
print (False and True)
print (False and False)


print("\nor operator\n")
print (True or  True)
print (True or  False)
print (False or  True)
print (False or  False)

print("\nnot operator\n")
print(not (True))
print(not(False))

# Assignment Operators

a=34
print(a)
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a%=5
print(a)
a//=5
print(a)
a**=5
print(a)

print("Hello , World! Welcome to Python.")

print("Twinkle twinkle, little star,\nHow I wonder what you are!")

name="Utkarsh"
age=20
height=5.7
is_student=True

print(name , age , height , is_student , sep=' , ')

a="45"
print(int(a) + 10)

food = str(input("What is  your favourite food?\n"))
print("Wow I also like",food)

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))

print ("The sum between two number is:" , a+b)
print ("The difference between two number is:" , a-b)
print ("The product of two number is:" , a*b)
print ("The quotient of two number is:" , a/b)

print('Harry said, "Python is awesome!" \n\nThis is on a new line.\n\nThis is a tab -> \t <- here ' )

a=int(input("Enter a number:"))
print("Square of the number is:" , a**2)
print("Cube of the number is:" , a**3)


a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)