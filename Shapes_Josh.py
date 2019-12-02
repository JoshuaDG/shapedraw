# Joshua Gonzalez
# Implements an application that keeps tracks of shapes
import turtle
import urllib.request
class Shape:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    # postcondition: returns whatever is needed for some drawing
    # tool to draw this kind of shape. Will be overridden in
    # descendant classes
    def get_shape_type(self):
        return "s"
    def to_string(self):
        return " %-2s %-6.2f %-7.2f " % (self.get_shape_type(),self.x,self.y)
    def get_draw_params(self):
        return [self.x, self.y]
'''
prconditin: all values must be integers
postcondition: takes the params of the circle and 
gives the x,y,radius to the Draw Shape Controller Class
'''
class Circle(Shape):
    def __init__(self,x=0,y=0,rad=0):
        super().__init__(x,y)
        self.radius = rad
    def get_shape_type(self):
        return "c"
    def to_string(self):
        return "%s %.2f" % (super().to_string(),self.radius)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend([self.radius])
        return result
'''
precondition: all values must be in integers
w and l must not be negative integers
postconition: give the params of the rectangle 
to the Turle Draw Shape Controller Class
'''
class Rectangle(Shape):
    def __init__(self,x=0,y=0,w=0,l=0):
        super().__init__(x,y)
        self.width = w
        self.length = l
    def get_shape_type(self):
        return "r"
    def to_string(self):
        return "%s %.2f %.2f" % (super().to_string(),self.length,self.width)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend([self.width, self.length])
        return result
        
'''
precondition: all values must be in integers and not string; 
l and s must not be negative
postcondition: set the length, sides, x and y for the polygon;
gets the angle of the corners by dividing the sides;
gives the result to the Turtle_Draw_Shape_Controller
'''
class Polygon(Shape):
    def __init__(self,x=0,y=0,l=0,s=0):
        super().__init__(x,y)
        self.length = l
        self.sides = s
        self.angle = 360/self.sides
    def get_shape_type(self):
        return "p"
    def to_string(self):
        return "%s %.2f %.2f %.2f" % (super().to_string(),self.length,self.sides,self.angle)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend([self.length,self.sides,self.angle])
        return result
 
class Turtle_Draw_Shape_Controller:
    def __init__(self):
        self.turtle = turtle.Turtle()
    #precondition: the turtle
    # has already been placed where the center of the circle is desired
    #postcondition: draws the circle of that radius
    def draw_circle(self,radius):
        self.turtle.circle(radius)
    #precondition: width and length are non-negative integers; the
    #turtle is already located where you want to be
    #postcondition: the rectangle will be drawn with specified
    #width and length. Turtle will be facing 0 degrees (x axis)
    #when this is done
    def draw_rect(self,width,length):
        self.turtle.setheading(0)
        self.turtle.forward(width)
        self.turtle.left(90)
        self.turtle.forward(length)
        self.turtle.left(90)
        self.turtle.forward(width)
        self.turtle.left(90)
        self.turtle.forward(length)
        self.turtle.left(90)
    #precondition: length,siedes are non - negative integers; turtle is already 
    # at the located where you want to draw at
    # postcondition: turtle will be draw in a specified angle and a set amount 
    # of sides
    def draw_polygon(self,length,sides,angle):
        self.turtle.setheading(0)
        for i in range(0,sides):
            self.turtle.forward(length)
            self.turtle.left(angle)
    #precondition: draw_shapes is a list of descendants of the
    # Shape class, Circle and Rectangle and repoly are supported.
    #postcondition: turtle graphics will be used to
    #draw the shapes on a turtle graphics canvas
    def draw_shapes(self,shapes):
        for shape in shapes:
            shape_type = shape.get_shape_type()
            params = shape.get_draw_params()
            self.turtle.penup()
            self.turtle.goto(int(params[0]),int(params[1]))
            self.turtle.pendown()
            if shape_type == "c":
                self.draw_circle(int(params[2]))
            elif shape_type == "r":
                self.draw_rect(int(params[2]),int(params[3]))
            elif shape_type == "p":
                self.draw_polygon(int(params[2]), int (params[3]),int(params[4]))
'''
precondition: Web_Retriever takes the name of the location of the code on the web
postcondition: changes the the location into a local file 
'''
class Web_Retriever:
    def chang_local(self,url):
        local = "shapes.txt"
        url_getter = urllib.request.URLopener()
        url_getter.retrieve(url,local)
        return local

'''
precondition: takes the name of the local file from the Class Web_Retriever
postcondition: read each line of the file, after that, goes through the file to look
for parameters for Circle, Rectangle, and Poly and return them all in a list.
'''
class Shape_XML_Parser:     
    def parse(self,fname):         
        file_var = open(fname,"r")         
        text = ""         
        for line in file_var:             
            text = text + line.strip()         
        shapes_list = []         
        poscir = text.find("<circle>")
        posrec = text.find("<rectangle>")
        pospoly = text.find("<regpoly>")
        #for the Circle Class
        while poscir >= 0:             
            endpos = text.find("</circle>",poscir+1)             
            tagbeg = text.find("<x>",poscir+1)             
            tagend = text.find("</x>",tagbeg+1)             
            x = float(text[tagbeg+3:tagend])             
            tagbeg = text.find("<y>",poscir+1)             
            tagend = text.find("</y>",tagbeg+1)             
            y = float(text[tagbeg+3:tagend])             
            tagbeg = text.find("<radius>",poscir+1) 
            tagend = text.find("</radius>",tagbeg+1)            
            radius = float(text[tagbeg+8:tagend])             
            cir = Circle(x,y,radius)             
            shapes_list.append(cir)             
            poscir = text.find("<circle>",endpos+9)
        # For the Rectangle Class
        while posrec >= 0:
            recendpos = text.find("</rectangle>",posrec+1)             
            rectagbeg = text.find("<x>",posrec+1)             
            rectagend = text.find("</x>",rectagbeg+1)             
            x = float(text[rectagbeg+3:rectagend])             
            rectagbeg = text.find("<y>",posrec+1)             
            rectagend = text.find("</y>",rectagbeg+1)             
            y = float(text[rectagbeg+3:rectagend])             
            rectagbeg = text.find("<length>",posrec+1) 
            rectagend = text.find("</length>",rectagbeg+1)            
            length = float(text[rectagbeg+8:rectagend])
            rectagbeg = text.find("<width>",posrec+1) 
            rectagend = text.find("</width>",rectagbeg+1)            
            width = float(text[rectagbeg+7:rectagend])
            rec = Rectangle(x,y,width,length)             
            shapes_list.append(rec)             
            posrec = text.find("<rectangle>",recendpos+9)
        #For the Polygon Class
        while pospoly >= 0:
            polyendpos = text.find("</regpoly>",pospoly+1)             
            tagbegpoly = text.find("<x>",pospoly+1)             
            tagendpoly = text.find("</x>",tagbegpoly+1)             
            x = float(text[tagbegpoly+3:tagendpoly])             
            tagbegpoly = text.find("<y>",pospoly+1)             
            tagendpoly = text.find("</y>",tagbegpoly+1)             
            y = float(text[tagbegpoly+3:tagendpoly])             
            tagbegpoly = text.find("<length>",pospoly+1) 
            tagendpoly = text.find("</length>",tagbegpoly+1)            
            length = float(text[tagbegpoly+8:tagendpoly])
            tagbegpoly = text.find("<sides>",pospoly+1) 
            tagendpoly = text.find("</sides>",tagbegpoly+1)            
            sides = float(text[tagbegpoly+7:tagendpoly])
            poly = Polygon(x,y,length,sides)             
            shapes_list.append(poly)             
            pospoly = text.find("<regpoly>",polyendpos+9)
        file_var.close()
        return shapes_list

url = "http://cs.lewisu.edu/~klumpra/2015Fall/shapes.xml"

web = Web_Retriever()
giveshape= Shape_XML_Parser()
drawer = Turtle_Draw_Shape_Controller()

local = web.chang_local(url) 
shapes = giveshape.parse(local)
drawer.draw_shapes(shapes)
for w in shapes:
    print(w.to_string())
