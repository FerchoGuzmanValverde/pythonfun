#Simple calculator in python

class Calculator:
  
  def DisplayOperations(self):
    print("SELECT OPERATION")
    print("Addition: 1")
    print("Substraction: 2")
    print("Multiplication: 3")
    print("Division: 4")
    print("End: 0")
  
  def MakeOperation(self, operation, num1:int, num2:int):
    match operation:
      case 1:
        print("The addition of %d + %d = %d" % (num1, num2, num1 + num2))
      case 2:
        print("The substraction of %d - %d = %d" % (num1, num2, num1 - num2))
      case 3:
        print("The multiplication of %d * %d = %d" % (num1, num2, num1 * num2))
      case 4:
        print("The division of %d / %d = %d" % (num1, num2, num1 / num2))

#Main program
cal = Calculator()
while(True):
  num1 = float(input("Input first number: "))
  num2 = float(input("Input second number: "))
  cal.DisplayOperations()
  op = int(input("Select operation: "))
  cal.MakeOperation(op, num1, num2) 
  if op == 0:
    break
  
  