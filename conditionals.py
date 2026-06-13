# if statement 

age=10

if(age>18):
    print("You are eligible")
    print("Thanks")

print("End of program")

# if-else statement

age=int(input("Enter your age:"))

if(age>18):
    print("You can drive")

else:
    print("You cannot drive")


# if-elif-else statement

age=int(input("Enter your age :"))

if(age>18):
    print("You can drive")

elif(age==18):
    print("Schedule an interview")

else:
    print('You cannot drive')



# Match casae

a=int(input("Enter a number between 1 and 10 :"))

match a:
    case 1:
        print("You won a car toy")
    case 5:
        print("You won 100ruppee")
    case 7:
        print("You won an ice cream")
    case _:
        print("Oops! Better luck next time ")


# for loops

for i in range(1,51):
    print(i)

for i in range(1,11):
    print("5 X" , i , "=" , 5*i)


# while loop  

i = 20
while i >= 1:
    print (i)
    i = i-1

i = 1
while i < 8:
    print (i)
    i = i+1

i = 1
while True:
    print (i)
    i = i+1


# break statement

for i in range(0,15):
    print(i)
    if i == 5:
        break

# continue statement

for i in range (1,20):
    if i == 10:
        continue
    print (i)


for i in range (1,20):

    print (i)
    if i == 10:
        continue

# pass statement

for i in range (5):
    
    if i == 3:
        pass
    print(i)
    


a=int(input("Enter a number:"))

if (a > 0):
    print("Its a positive number")

elif (a < 0):
    print("The number is a negative number ")

else:
    print("The number is zero")

age = int(input("Enter your age :"))

if (age >= 18):
    print(" You are eligible to vote ")

else:
    print(" You are not eligible to vote")



num = int(input("Enter a number :"))

if (num % 2 == 0):
    print("Its an even number ")

else:
    print("Its an odd number")

a=int(input("Enter a number between 1 and 7:\n"))

match a:
    case 1:
        print("Sunday")

    case 2:
        print("Monday")

    case 3:
        print("Tuesday")

    case 4:
        print("Wednesday")

    case 5:
        print("Thursday")

    case 6:
        print("Friday")

    case 7:
        print("Saturday")


num1= int(input("Enter first number:\n"))
num2= int(input("Enter second number:\n"))

operation = input("Choose an operation:")

match operation:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "*":
        print(num1 * num2)

    case "/":
        print(int(num1 / num2))



for i in range (1,11):
    print(i)


n = int(input("Enter a number:"))

for i in range(1,11):
    print(n ,"X" , i , "=", n*i)

sum=0
for i in range (1,101):
    sum+= i

print(sum)
 

for i in range (1,5):
    print("*" * i)


sum = 0
i=1

while i<=10:
    print(i)
    sum+=i
    i += 1

print(sum)

password= "BJHJ123"
entered_password=input("Enter password:") 

while(entered_password != password):
    entered_password = input("Oops wrong password! Try Again :")

print("Successfully! Logged in")


num=44556

print(int(str(num)[::-1]))


for i in range(1,11):
    if i==7:
        break
    print(i)


for i in range(1,11):
    if i==5:
        continue
    print(i)


for i in range (1,6):
    if i == 3:
        pass
    print(i)




n = int(input().strip())


if n % 2 != 0:
    print("Weird")
    
else:
    if 2 <= n <= 5:
        print("Not Weird")

    elif 6 <= n <= 20:
        print("Weird")
    
    elif n > 20:
        print("Not Weird")


n= int(input())
for i in range (1 , n+1):
        print(i , end="")