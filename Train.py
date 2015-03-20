# Course: CS 1MD3
# Name:  Barane Paramanathan
# File: assign4.py
# Description: Program which runs a train across the screen


from graphics import*
from time import*

# Wheels are common to BoxCar, PassengerCar, Caboose, and Locomotive
class Wheels:

    # constructor of class Wheels
    def __init__(self, win, b, length, height, r, colour):
        """ Creates wheels for a car whose box left-top
            corner is located at the point 'b', the box dimensions
            are 'length' and 'height'. r is the wheels radius. The
            wheels are drawn in the graphics window 'win' in the
            colour given in the variable 'colour' """ 

        p1 = Point(b.getX()+((length-(4*r))/3)+r, b.getY()+height)
        self.Wheels = Circle(p1,r) #Front wheel
        self.Wheels.setFill(colour)

        p2 = Point(b.getX()+(length-((length-(4*r))/3))-r, b.getY()+height)        
        self.Wheels2 = Circle(p2,r)#backwheel
        self.Wheels2.setFill(colour)
        
        self.Wheels.draw(win)
        self.Wheels2.draw(win)
    #end of constructor

    # method move -- moves the wheels dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.Wheels.move(dx,dy)
        self.Wheels2.move(dx,dy)
#end of class Wheels




# Box is common to BoxCar, PassengerCar, Caboose, and Locomotive 
class Box:

    # the constructor
    def __init__ (self, win, b, length, height, colour):
        """ Creates box for a car whose left-top corner is located
            at the point 'b', the box dimensions are 'length' and 'height'.
            The box is drawn in the graphics window 'win' in the
            colour given in the variable 'colour' """ 

        p1 = Point(b.getX()+length, b.getY()+height)
        self.box = Rectangle(b,p1)
        self.box.setFill(colour)

        self.box.draw(win)
    #end of constructor

    # method move -- moves the box dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.box.move(dx,dy)
    #end of move
#end of class Box


# BoxCar uses Wheels and Box
class BoxCar:


    # the constructor
    def __init__ (self, win, b, length, height, radius, box_colour,
                  wheel_colour):
        """ Creates a boxcar with a box given by 'b', 'length', 'height'
            and wheels given by 'b', 'length', 'height', and 'radius'.
            The box is to have colour 'box_colour', the wheels are
            to have colour 'wheel_colour'. The box car is drawn in
            the graphics window 'win' """ 
        
        self.Wheels = Wheels(win, b, length, height, radius, wheel_colour)
        self.Box = Box(win, b, length, height, box_colour)

        p2 = Point(b.getX()+(length-((length*2)/3)), b.getY()+(height-(2*height/3)))
        p3 = Point(b.getX()+(length-(length/3)), b.getY()+height)
        self.door = Rectangle(p2,p3)
        self.door.draw(win)
    #end of constructor

    # method move -- moves box car dx along the x axis and dy along the y axis
    def move(self, dx, dy):
        self.Wheels.move(dx,dy)
        self.Box.move(dx,dy)
        self.door.move(dx,dy)

    #end of move
#end of class BoxCar


# PassengerCar uses Wheels and Box
class PassengerCar:

    # the constructor
    def __init__ (self, win, b, length, height, radius, box_colour,
                  wheel_colour):
        """ Creates a passenger car with a box given by 'b', 'length',
            'height' and wheels given by 'b', 'length', 'height', and
            'radius'. The box is to have colour 'box_colour', the wheels
            are to have colour 'wheel_colour'. The box car is drawn in
            the graphics window 'win' """

        self.Wheels = Wheels(win, b, length, height, radius, wheel_colour)
        self.Box = Box(win, b, length, height, box_colour)

        #Draws first window
        p2 = Point(b.getX()+(length/11), b.getY()+(height/4))
        p3 = Point(b.getX()+(2*(length/11)), b.getY()+(height/4)+(height/2))
        self.window = Rectangle(p2,p3)
        self.window.draw(win)
        self.window.setFill("black")


        #Draws second window
        p2 = Point(b.getX()+(3*(length/11)), b.getY()+(height/4))
        p3 = Point(b.getX()+(4*(length/11)), b.getY()+(height/4)+(height/4))
        self.window2 = Rectangle(p2,p3)
        self.window2.draw(win)
        self.window2.setFill("blue")

        
        #Draws the third window
        p2 = Point(b.getX()+(5*(length/11)), b.getY()+(height/4))
        p3 = Point(b.getX()+(6*(length/11)), b.getY()+(height/4)+(height/4))
        self.window3 = Rectangle(p2,p3)
        self.window3.draw(win)
        self.window3.setFill("blue")

        #Draws the forth window
        p2 = Point(b.getX()+(7*(length/11)), b.getY()+(height/4))
        p3 = Point(b.getX()+(8*(length/11)), b.getY()+(height/4)+(height/4))
        self.window4 = Rectangle(p2,p3)
        self.window4.draw(win)
        self.window4.setFill("blue")

        #Draws the fifth window
        p2 = Point(b.getX()+(9*(length/11)), b.getY()+(height/4))
        p3 = Point(b.getX()+(10*(length/11)), b.getY()+(height/4)+(height/2))
        self.window5 = Rectangle(p2,p3)
        self.window5.draw(win)
        self.window5.setFill("black")
    #end of constructor
        
    # method move -- moves the passenger car dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.Wheels.move(dx,dy)
        self.Box.move(dx,dy)
        self.window.move(dx,dy)
        self.window2.move(dx,dy)
        self.window3.move(dx,dy)
        self.window4.move(dx,dy)
        self.window5.move(dx,dy)
    #end of move
#end of class PassengerCar





# Caboose uses Wheels and Box
class Caboose:

    def __init__(self, win, b, length, height, radius, box_colour,
                 wheel_colour, bubble_colour):
        """ Creates a caboose with a box given by 'b', 'length', 'height' and
            of colour 'box_colour'. The wheels are given by 'b', 'length',
            'height', 'radius' and are of colour 'wheel_colour'. The bubble's
            dimensions are determined from the dimensions of the box, its
            colour is given by 'bubble_colour'. The caboose is drawn in the
            graphics window 'win' """

        #Draws object on top of cart
        p1 = Point(b.getX()+(length/4), b.getY()-(height/4))
        p2 = Point(b.getX()+length-(length/4), b.getY()+(height/4))

        self.oval = Oval(p1, p2)
        self.oval.draw(win)
        self.oval.setFill(bubble_colour)

        self.Wheels = Wheels(win, b, length, height, radius, wheel_colour)
        self.Box = Box(win, b, length, height, box_colour)
        

    #end of constructor

    #method move -- moves caboose dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.Wheels.move(dx,dy)
        self.Box.move(dx,dy)
        self.oval.move(dx,dy)
    #end of move
#end of class Caboose



        
# uses Box and Wheels
class Locomotive:

    # the constructor
    def __init__(self, win, b, length, height, radius, box_colour,
                 cowcatcher_colour, wheel_colour, smokestack_colour,
                 cabin_colour):
        """ Creates a locomotive with a box given by 'b', 'length', 'height'
            and of colour 'box_colour'. The wheels are given by 'b', 'length',
            'height', 'radius' and are of colour 'wheel_colour'. The cowcatcher
            colour is given by 'cowcatcher_colour'. The smokestack's colour
            is given by 'smokestack_colour'. The cabin colour is given by
            'cabin_colour'. The dimensions of the cowcatcher are determined
            from the dimension of the box. The dimensions of the smokestack
            are determined from the dimensions of the box. The dimensions of
            the cabin are determined from the dimensions of the box. The
            locomotive is drawn in the graphics window 'win' """

        #Draw the smoke stack
        p1 = Point(b.getX()+(length/8), b.getY()-(height/3))
        p2 = Point(b.getX()+(length/4), b.getY())
        self.smokestack = Rectangle(p1,p2)
        self.smokestack.draw(win)
        self.smokestack.setFill(smokestack_colour)

        #Draw the cabin
        p2 = Point(b.getX()+length-(length/3), b.getY()-(height/2))
        p3 = Point(b.getX()+length, b.getY())
        self.cabin = Rectangle(p2,p3)
        self.cabin.draw(win)
        self.cabin.setFill(cabin_colour)

        #Draw the cow catcher
        p4 = Point(b.getX(), b.getY())
        p5 = Point(b.getX(), b.getY()+height)
        p6 = Point(b.getX()-(length/6), b.getY()+height)
        self.cowcatcher = Polygon(p4,p5,p6)
        self.cowcatcher.draw(win)
        self.cowcatcher.setFill(cowcatcher_colour)
        

        #Draw the wheels and box
        self.Wheels = Wheels(win, b, length, height, radius, wheel_colour)
        self.Box = Box(win, b, length, height, box_colour)
        
    #end of constructor

    # method move -- moves locomotive dx along x axis and dy along y axis
    def move(self, dx, dy):
        self.Wheels.move(dx,dy)
        self.Box.move(dx,dy)
        self.smokestack.move(dx,dy)
        self.cabin.move(dx,dy)
        self.cowcatcher.move(dx,dy)
    #end of move
#end of class Locomotive

    

class Tracks:

    # the constructor
    def __init__(self, win, height):
        """ create tracks in black colour """
        # create tracks as a thin long rectangle
        self.tracks = Rectangle(Point(4,196-height),Point(1196,196))
        self.tracks.setFill('black')   # make it black
        self.tracks.draw(win)          # draw it
#end of class Tracks



class Train:

    # the constructor
    def __init__(self, win):
        """ assemble a train and draw it in the graphics window win """
        length = 60
        height = 30
        radius = 8
        
        self.locomotive = Locomotive(win, Point(750, 156),length,height, radius,"black", "brown", "black", "grey", "grey")
        self.caboose = Caboose(win, Point(815, 156),length,height, radius,"blue", "black", "red")
        self.passengercar = PassengerCar(win, Point(880, 156),length,height, radius,"red", "black")
        self.passengercar2 = PassengerCar(win, Point(945, 156),length,height, radius,"green", "black")
        self.boxcar = BoxCar(win, Point(1010, 156),length, height, radius,"yellow", "black")
        self.boxcar2 = BoxCar(win, Point(1075, 156),length, height, radius,"blue", "black")
        self.caboose2 = Caboose(win, Point(1140, 156),length,height, radius,"red", "black", "blue")

     
    #end of constructor

    # method move -- moves train dx along x axis and dy along y-axis
    def move(self, dx, dy):
        self.locomotive.move(dx,dy)
        self.caboose.move(dx,dy) 
        self.passengercar.move(dx,dy)
        self.passengercar2.move(dx,dy)
        self.boxcar.move(dx,dy)
        self.boxcar2.move(dx,dy)
        self.caboose2.move(dx,dy)
        
    #end of move

    #method getStart -- returns the position of the front of the train
    def getStart(self):
        """ Your code goes here """
    #end of getStart()
#end of class Train



# function main()
def main():
    win = GraphWin("Train",1200,200)   # create the required graphics window
    tracks = Tracks(win,2)             # create and display the tracks
    train = Train(win)                 # create and display train in the starting position
    original = train.getStart()        # remember starting position
    start = 0

    #Displays first message
    message = Text(Point(600, 20), "Click to start")
    message.draw(win)
    win.getMouse()
    message.undraw()

    #Starts train
    while (start < 10):
        train.move(-20,0)
        start=start+1
        sleep(.05)


    #Reverses train
    while (start > 0):
        train.move(-10,-10)
        start=start-1
        sleep(.05)


    while (start < 10):
        train.move(-20,0)
        start=start+1
        sleep(.05)

    #Displays third message
    message = Text(Point(600,20), "Click to terminate")
    message.draw(win)
    win.getMouse()
    win.close()

#end of main()


# the executable part of the program
main()  # execute main()
# program terminates
