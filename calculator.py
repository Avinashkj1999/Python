
def add(n1,n2):
 add = n1+n2
 return add

def subtract(n1,n2):
 subtract = n1-n2
 return subtract

def multiply(n1,n2):
 multiply = n1*n2
 return multiply

def divison(n1,n2):
 division = n1/n2
 return division

print("Select operation.")
print("+")
print("-")
print("*")
print("/")

def calculator():
 
 choice=input("Enter the operation you want to perform: ")
 if choice in ('+','-','*','/'):
  try:
   num1=float(input("Enter first number: "))
   num2= float(input("Enter second number: "))
  except ValueError:
   print("Invalid input. Please enter a number.")
  
 if choice == '+':
  print(num1, "+", num2, "=", add(num1, num2))

 elif choice == '-':
  print(num1, "-", num2, "=", subtract(num1, num2))

 elif choice == '*':
  print(num1, "*", num2, "=", multiply(num1, num2))

 elif choice == '/':
  print(num1, "/", num2, "=", divison(num1, num2))

calculator()
next_calculation = input("Let's do next calculation? (yes/no): ")
while next_calculation != "no":
 calculator()
 next_calculation = input("Let's do next calculation? (yes/no): ")


