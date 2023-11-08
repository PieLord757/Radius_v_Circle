import math
import random
radius = int(input('What is the radius of the circle?'))
area = int(input('What is the area of the square?'))
list = ['Circle', 'Square']
def circle_or_square(radius, area):
  if math.pi*radius*2 > (area**(1/2))*4:
    return True
  elif (area**(1/2))*4 > math.pi*radius*2:
    return False
  else:
    return True
    Print(f'They are equal. I just like {random.choices(list)} more')  
print(circle_or_square(radius,area))

