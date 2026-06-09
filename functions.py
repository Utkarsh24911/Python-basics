# def average (a,b,c):
#     d = (a+b+c)/3.0
#     # print(d)

#     return d 

# o1 = average(4,3,2)
# o2 = average(1,3,4)

# print(o1)
# print(o2)

# def add(a,b): #here a nad b are parameters and these are positional argument
#     x = a+b
#     return x

# c = add(3,6) # values here are arguments
# print (c)/

# def add (a,b,plus=0): # here plus = 0 is a default value of default argument 
#     x = a + b + plus
#     return x 

# c = add(3,5,6) #and here putting value of plus = 6 not zero then the value of plus = 6 is passed and then it will added to a+b+plus
# print(c)


# def add (a,b,):
#     x=a+b
#     return x

# c = add(5,7)
# print (c)

# c1= add(b=7, a=5) # here we pass the value of b first then value of a this is keyword argument
# print(c1)

# lambda function

# square = lambda x : x*x
# sum = lambda x,y:x+y

# # lambda function is use for one liner function as we can write the above code instead of  
# # def add (a,b,):
# #     x=a+b
# #     return x

# # c = add(5,7)
# # print (c)



# print(square(5))
# print(sum(99,99))


# RECURSION

# fibonacci series = sum of pervious 2 no.

# 0 1 1 2 3 5 8 13 21 and so on
# 0 1 2 3 4 5 6 7  8 index no.

# fib(0)= 0
# fib(1)= 1
# fib(2)=fib(0) + fib(1)

# fib(n)=fib(n-2) + fib(n-1)

# def fib(n):
#     # Base case in recursiom 
#     if(n==0 or n==1):
#         return n
    
#     return fib(n-2) + fib(n-1)
# print (fib(6)) 



# def factorial(n):
#     # base case in recursiom
#     if (n == 0 or n == 1):
#         return 1
    
#     return  n * factorial(n-1)
# print (factorial(5))



# def sum(a,b):
# # here a and b are local scope inside a function where Variables declared inside a function are accessible only within that function.
#     c=a+b
#     print(z)
#     return c

# z=66# z is a global scobe and accessible everywhere where Variables declared inside a function are accessible only within that function.

# print(sum(4,6))

# def sum (a,b):
#     '''This will sum two numbers'''
#     c =a+b
#     return c

# print(sum.__doc__)      

# def  greet():
#            print("Hello , Python learner!")

# greet()


# square =lambda x: x * x
# print(square(4))

# def full_name(first , last):
#     return f"{first} {last}"

# print (full_name("John" , "Doe")) 

# def calculate_area(lenght ,widht=10):
#     return lenght * widht

# print(f"The area of this rectangle is {calculate_area(12)}")

# print(f"The area of other rectangle is {calculate_area(12 , 15)}")

# sum = lambda x,y : x+y
# print(sum(10,12))


# square = lambda x:x*x
# list1 = [1,2,3,4,5]

# print(list(map(square,list1)))


# def factorial(n):
#     if(n==0 or n==1):
#         return 1
    
#     return n* factorial(n-1)
# print(factorial(5))


# def sum_of_digit(n):
#     if n==0 :
#         return 0
    
#     return n%10 + sum_of_digit(n//10)

# print(sum_of_digit(7532))


# Global variable
balance = 1000.00

# 1. Function with no parameters and no return value
# Qodo: Test this function
def check_balance():
    print("Your current balance is: " + str(balance))

print("Checking balance for the first time:")
check_balance()

print("\n" + "-"*30 + "\n") # Separator for clarity


# 2. Function with parameters and no return value
# Qodo: Test this function
def update_balance(amount):
    new_balance = balance + amount
    print("Balance updated successfully. New balance: " + str(new_balance))

print("Updating balance by adding 500.00:")
update_balance(500.00)

print("\n" + "-"*30 + "\n")


# 3. Function with parameters and a return value
def calculate_total_bill(rate, quantity):
    total = rate * quantity
    return total

print("Calculating total bill for Order A:")
total_a = calculate_total_bill(10.00, 5)
print(type(total_a))
print("Total for Order A: " + str(total_a))

print("\n" + "-"*30 + "\n")


# 4. Function with default parameter value
# Qodo: Test this function
def calculate_total_bill_with_tax(rate, quantity, tax_rate=0.05):
    total = rate * quantity
    total_with_tax = total + (total * tax_rate)
    return total_with_tax

# This section is ready for when your instructor covers variable number of arguments (*args)
# 5. #function with variable number of arguments
    # 5. Function that returns a value
def new_function(a, b, c):
    total_sum = a + b + c
    print("This is a new function that returns a value.")
    return total_sum

# Call the function by passing 3 numbers (e.g., 10, 20, 30)
combined_sum = 5 + new_function(10, 20, 30)

print("Sum of 5 and the return value of new function: " + str(combined_sum))

