# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def area_triangle(base,height):
  area = (1/2)*base*height
  return area

base = 5
height = 9
print(area_triangle(base,height))

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width

def calculate_area(dimension1,dimension2,shape="triangle"):
   '''
:param dimension1: In case of triangle it is "base". For rectangle it is "length".
:param dimension2: In case of triangle it is "height". For rectangle it is "width".
:param shape: Either "triangle" or "rectangle"
:return: Area of a shape
 '''

   if shape=="triangle":
    area=1/2*(dimension1*dimension2) # Triangle area is : 1/2(Base*Height)
   elif shape=="rectangle":
    area=dimension1*dimension2 # Rectangle area is: Length*Width
   else:
    print("Error: Input shape is neither triangle nor rectangle.")
    area=None # If user didn't supply "triangle" or "rectangle" as shape then return Non
   return area

base = 6
height = 6
print(calculate_area(base,height))

# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print

# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)


def print_pattern(n=5):
  '''
  :param n: Integer number representing number of lines
  to be printed in a pattern. If n=3 it will print,
    *
    **
    ***
  If n=4, it will print,
    *
    **
    ***
    ****
  Default value for n is 5. So if function caller doesn't
  supply the input number then it will assume it to be 5
  :return: None
  '''
  # we need to run two for loops. Outer loop prints patterns line by line
  # where as inner loop print the content of that specific lines
  for i in range(n):
      s = ''
      for j in range(i+1):
          s = s + '*'
      print(s)



  


  
