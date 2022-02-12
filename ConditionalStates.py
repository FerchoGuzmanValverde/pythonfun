#This simple block indicates if a person has a salary bigguer than 3000 must pay taxas

salary = int(input("Input a salary: "))
if salary > 3000:
  print("You must pay taxas")
else:
  print("You don´t pay taxas")
  
#This block determines the bigguer number

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
if num1 > num2:
  print("Number %d is greater than %d" % (num1, num2))