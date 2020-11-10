import turtle

s = turtle.getscreen()
t = turtle.Turtle()
s.setup(400,400)
s.bgcolor("yellow")
t.fillcolor("green")
class shape:
    def __init__(self,length = 0) :
   
        self.length = length


class polygon(shape):
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional  with straight sides.")
        
class square(polygon):
    def area(self):
    	print(self.length**2)
    def perimeter(self):
    	print(4*self.length)
    def show(self):
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
    

class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 

class hexagon(polygon):
    def show(self):
      
        for i in range(6):
           t.begin_fill()
           t.forward(self.length) 
           t.right(60)
           t.end_fill()

class octagon(polygon):
    def show(self):
        for i in range(8):
           t.forward(self.length) 
           t.right(45)

class triangle(polygon):
    
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)     
class circle:
	def __init__(self,r):
		self.radius=r
	def area(self):
		return self.radius**2*3.14
	def show(self):
		t.circle(self.radius)

hex1 = hexagon(100)
hex1.info()
hex1.show()

pent1=pentagon(75)
pent1.info()
pent1.show()

tri1 = triangle(100)
tri1.info()
tri1.show()

sq1=square(75)
sq1.info()
sq1.show()

oct1=octagon(75)
oct1.info()
oct1.show()

cir=circle(100)
print(cir.area())
cir.show()
