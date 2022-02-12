class Area:
  
  global side
  side = float(input("Input size: "))
  
  def calculateArea():
    area = side * side
    return "The area of the square is: " + str(area)

print(Area.calculateArea())