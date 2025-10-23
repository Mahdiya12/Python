class Rectangle(): 

   def __init__(self, l, w):
      self.length = l
      self.width = w

   def areaRectangle(self):

      return self.length * self.width  
   
newRectangle = Rectangle(10, 20)   
print("Dimension of rectangle widht = %d , length = %d " %(newRectangle.width , newRectangle.length)) 

print("Area of rectangle is" , newRectangle.areaRectangle())