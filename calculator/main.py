import os
import art

# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(art.logo)
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  calculator_active = True
  
  while calculator_active:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  # Additional computations
    user_continue_choice = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ")
    if user_continue_choice == "y":
      num1 = answer
    else:
      calculator_active = False
      os.system('clear')
      calculator()

calculator()