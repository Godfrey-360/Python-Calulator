import math


print("========================================================")
print("                  GME CALCULATOR                              ")
print("========================================================")



def operator():
 print("**************************")   
 print("1.ADDITION")
 print("2.SUBSTRACTION")
 print("3.MULTIPLICATION")
 print("4.DIVISION")
 print("5.SQUARE")
 print("6.SQUARE-ROOT")
 print("7.EXPONET")
 print("8.LOG")

 print("**************************")

 no = int(input("Enter operator: "))
 if no == 1:
    print(additon())    

 elif no == 2:
    print(substraction())

 elif no == 3:
    print(multiplication())

 elif no  == 4:
    print(division())

 elif no == 5:
   print(square())

 elif no == 6:
   print(squareroot())

 elif no == 7:
   print(exponet())  

 elif no == 8:
   print(log())    

 else:
    print("Enter the right choice")       

 


def additon():
 x= float(input("Enter first value: "))
 y = float(input("Enter second value: "))
 print("==========")
 return x+y
 


def substraction():
 x= float(input("Enter first value: "))
 y = float(input("Enter second value"))
 print("=========")
 return x-y 


def multiplication():
 x= float(input("Enter first value: "))
 y = float(input("Enter second value: "))
 print("===========")
 return x*y 



def division():
 x= float(input("Enter first value: "))
 y = float(input("Enter second value: "))
 print("===========")
 return x/y 

def square():
   print("==================")
   x = float(input("Enter value: "))
   print(f"The square of {x} is {x*x}")

def squareroot():
   print("==================")
   x = float(input("Enter value: "))
   print(f"The square-root of {x} is {math.sqrt(x)}")

def exponet():
   print("===================")
   x = float(input("Enter value: ")) 
   print (f"The exponet of {x} is {math.exp(x)}") 

def log():
   print("==================")
   x = float (input("Enter value: "))
   print (f"The log of {x} is {math.log(x)}") 


operator()
