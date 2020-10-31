from graphics import *
from random import *


class Dice:
    def __init__(self):
        self.dice = [0]*2
        self.roll()
        
    def roll(self):
        for pos in range(2):
            self.dice[pos] = randrange(1,7)
            
    def score(self):
        score = []
        for value in self.dice:
            score.append(value)
        return score

    def values(self):
        return self.dice[:]

class DieView:
    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""
    
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
           d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win            # save this for drawing pips later
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size   # radius of each pip
        hsize = size / 2.0        # half the size of the die
        offset = 0.6 * hsize      # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)
        
        # Draw an initial value
        self.setValue(1)

    def __makePip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        "Set this die to display value."
        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        # turn correct pips on
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)        
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)

class GraphicInterface:
    
    def __init__(self):
        self.win = GraphWin("P A R C H E E S I", 800, 600)
        

        
        self.win.setBackground("lightcyan")

        Turns = Text(Point(50,25), "Turns:")
        Turns.setSize(15)
        Turns.draw(self.win)

        Instructions = Text(Point(700, 200), "Press R to roll the dice after\nyour icon/color shows up in\nthe turn order.\n\nPress Esc at any time\nto exit the game.")
        Instructions.setSize(10)
        Instructions.draw(self.win)

        P1 = Text(Point(130, 25), "Player 1")
        P1.setSize(15)
        P1.draw(self.win)
        P2 = Text(Point(230, 25), "Player 2")
        P2.setSize(15)
        P2.draw(self.win)
        P3 = Text(Point(330, 25), "Player 3")
        P3.setSize(15)
        P3.draw(self.win)
        P4 = Text(Point(430, 25), "Player 4")
        P4.setSize(15)
        P4.draw(self.win)

        self.players = [P1, P2, P3, P4]
        
        Frame = Rectangle(Point(30, 50), Point(570, 590))
        Frame.setFill("papayawhip")
        Frame.draw(self.win)

        blueBase = Circle(Point(125,145), 81)
        blueBase.setFill("lightblue")
        blueBase.setWidth(2)
        blueBase.draw(self.win)

        yellowBase = Circle(Point(475,145), 81)
        yellowBase.setFill("khaki")
        yellowBase.setWidth(2)
        yellowBase.draw(self.win)

        greenBase = Circle(Point(475,495), 81)
        greenBase.setFill("lightgreen")
        greenBase.setWidth(2)
        greenBase.draw(self.win)

        redBase = Circle(Point(125,495), 81)
        redBase.setFill("lightcoral")
        redBase.setWidth(2)
        redBase.draw(self.win)

        self.blueSquares = [[0]*7]*3
        for i in range(3):
            for j in range(7):
                self.blueSquares[i][j]= Rectangle(Point(219+(i*54), 50+(j*27)),Point(273+(i*54), 77+(j*27)))
                if((i == 0 and j == 4) or (i == 1 and j >0)):
                   self.blueSquares[i][j].setFill("lightblue")
                elif((i==1 and j==0) or (i == 2 and j ==4)):
                    self.blueSquares[i][j].setFill("lightgray")
                self.blueSquares[i][j].draw(self.win)
        self.lastBlue = Rectangle(Point(273, 239), Point(327, 266))
        self.lastBlue.setFill("lightblue")
        self.lastBlue.draw(self.win)

        self.redSquares = [[0]*7]*3
        for i in range(3):
            for j in range(7):
                self.redSquares[i][j]= Rectangle(Point(30+(j*27), 401-(i*54)),Point(57+(j*27),347-(i*54)))
                if((i == 0 and j == 4) or (i == 1 and j >0)):
                    self.redSquares[i][j].setFill("lightcoral")
                elif((i==1 and j==0) or (i == 2 and j ==4)):
                    self.redSquares[i][j].setFill("lightgray")
                self.redSquares[i][j].draw(self.win)
        self.lastRed = Rectangle(Point(219, 347), Point(246, 293))
        self.lastRed.setFill("lightcoral")
        self.lastRed.draw(self.win)


        self.greenSquares = [[0]*7]*3
        for i in range(3):
            for j in range(7):
                self.greenSquares[i][j]= Rectangle(Point(327-(i*54), 590-(j*27)),Point(381-(i*54), 563-(j*27)))
                if((i == 0 and j == 4) or (i == 1 and j >0)):
                    self.greenSquares[i][j].setFill("lightgreen")
                elif((i==1 and j==0) or (i == 2 and j ==4)):
                    self.greenSquares[i][j].setFill("lightgray")
                self.greenSquares[i][j].draw(self.win)
        self.lastGreen = Rectangle(Point(273, 401), Point(327, 374))
        self.lastGreen.setFill("lightgreen")
        self.lastGreen.draw(self.win)


        self.yellowSquares = [[0]*7]*3
        for i in range(3):
            for j in range(7):
                self.yellowSquares[i][j]= Rectangle(Point(570-(j*27), 239+(i*54)),Point(543-(j*27),293+(i*54)))
                if((i == 0 and j == 4) or (i == 1 and j >0)):
                    self.yellowSquares[i][j].setFill("khaki")
                elif((i==1 and j==0) or (i == 2 and j ==4)):
                    self.yellowSquares[i][j].setFill("lightgray")
                self.yellowSquares[i][j].draw(self.win)
        self.lastYellow = Rectangle(Point(381, 347), Point(354, 293))
        self.lastYellow.setFill("khaki")
        self.lastYellow.draw(self.win)

        blueHome = Polygon(Point(273, 266), Point(260, 279), Point(300, 320), Point(340, 279), Point(327, 266))
        blueHome.setFill("lightblue")
        blueHome.draw(self.win)
        
        redHome = Polygon(Point(246, 293), Point(260, 279), Point(300, 320), Point(260, 360), Point(246, 347))
        redHome.setFill("lightcoral")
        redHome.draw(self.win)

        greenHome = Polygon(Point(273, 374), Point(260, 360), Point(300, 320), Point(340, 360), Point(327, 374))
        greenHome.setFill("lightgreen")
        greenHome.draw(self.win)

        yellowHome = Polygon(Point(354, 347), Point(340, 360), Point(300, 320), Point(340, 279), Point(354, 293))
        yellowHome.setFill("khaki")
        yellowHome.draw(self.win)

        l1 = Line(Point(260, 279), Point(219, 239))
        l1.draw(self.win)
        l2 = Line(Point(260, 360), Point(219, 401))
        l2.draw(self.win)
        l3 = Line(Point(340, 279), Point(381, 239))
        l3.draw(self.win)
        l4 = Line(Point(340, 360), Point(381, 401))
        l4.draw(self.win)
        

        line = Line(Point(600, 0), Point(600, 600))
        line.setWidth(3)
        line.draw(self.win)

        self.createDice(Point(810, 50), 50)

    def createPieces(self):
        self.green = [0]*4
        self.blue = [0]*4
        self.red = [0]*4
        self.yellow = [0]*4

        self.blueFinish = [0]*4
        self.redFinish = [0]*4
        self.greenFinish = [0]*4
        self.yellowFinish = [0]*4

        self.greenMoved = [0]*4
        self.blueMoved = [0]*4
        self.redMoved = [0]*4
        self.yellowMoved = [0]*4

        self.greenHome = [1]*4
        self.blueHome = [1]*4
        self.redHome = [1]*4
        self.yellowHome = [1]*4
        
        for i in range(4):
            self.blue[i] = Circle(Point(80+(i*30),145),10)
            self.blue[i].setFill("steelblue")
            self.blue[i].setWidth(3)
            self.blue[i].draw(self.win)

        for i in range(4):
            self.green[i] = Circle(Point(430+(i*30),495),10)
            self.green[i].setFill("green")
            self.green[i].setWidth(3)
            self.green[i].draw(self.win)

        for i in range(4):
            self.red[i] = Circle(Point(80+(i*30),495),10)
            self.red[i].setFill("red")
            self.red[i].setWidth(3)
            self.red[i].draw(self.win)

        for i in range(4):
            self.yellow[i] = Circle(Point(430+(i*30),145),10)
            self.yellow[i].setFill("palegoldenrod")
            self.yellow[i].setWidth(3)
            self.yellow[i].draw(self.win)


    def start(self, piece):
        i = 0
        if piece == "blue":
            while(self.blueHome[i]==0):
                i+=1
                if i ==3 and self.blueHome[i]==0:
                    self.move(piece, 5)
                    break
            
            self.blue[i].undraw()
            self.blue[i] = Circle(Point(233,171),10)
            self.blue[i].setFill("steelblue")
            self.blue[i].setWidth(3)
            self.blue[i].draw(self.win)

            self.blueHome[i]=0
            print(self.blueHome)
                          
        elif piece == "yellow":
            i = 0        
            while(self.yellowHome[i]==0):
                i+=1
                if i ==3 and self.yellowHome[i]==0:
                    self.move(piece, 5)
                    break
                          
            self.yellow[i].undraw()
            self.yellow[i] = Circle(Point(449,253),10)
            self.yellow[i].setFill("palegoldenrod")
            self.yellow[i].setWidth(3)
            self.yellow[i].draw(self.win)

            self.yellowHome[i]=0
            print(self.yellowHome)
                          
        elif piece == "red":
            i = 0        
            while(self.redHome[i]==0):
                i+=1
                if i ==3 and self.redHome[i]==0:
                    self.move(piece, 5)
                    break
                          
            self.red[i].undraw()
            self.red[i] = Circle(Point(151,387),10)
            self.red[i].setFill("red")
            self.red[i].setWidth(3)
            self.red[i].draw(self.win)

            self.redHome[i]=0
            print(self.redHome)
                          
        elif piece == "green":
            i = 0        
            while(self.greenHome[i]==0):
                i+=1
                if i ==3 and self.greenHome[i]==0:
                    self.move(piece, 5)
                    break
                          
            self.green[i].undraw()
            self.green[i] = Circle(Point(367,469),10)
            self.green[i].setFill("green")
            self.green[i].setWidth(3)
            self.green[i].draw(self.win)

            self.greenHome[i]=0
            print(self.greenHome)
            
    def captured(self, colour, i):
        if colour ==  "blue":
            color = "steelblue"
            piece = self.blue
            home = self.blueHome
            moved = self.blueMoved
            coordinates = Point(80,145)
        elif colour ==  "red":
            color = "red"
            piece = self.red
            home = self.redHome
            moved = self.redMoved
            coordinates = Point(80,495)
        elif colour ==  "green":
            color = "green"
            piece = self.green
            home = self.greenHome
            moved = self.greenMoved
            coordinates = Point(430,495)
        elif colour ==  "yellow":
            color = "palegoldenrod"
            piece = self.yellow
            home = self.yellowHome
            moved = self.yellowMoved
            coordinates = Point(430,145)

        for j in range(len(home)):
            if home[j] ==0:
                piece[i].undraw()
                piece[i] = Circle(Point(coordinates.getX()+j*30, coordinates.getY()), 10)
                piece[i].setFill(color)
                piece[i].setWidth(3)
                piece[i].draw(self.win)
                home[j] = 1
                moved[j] = 0
                
                break
                

    def move(self, color, n):
        done = False
          
        if color ==  "blue":
            piece = self.blue
            moved = self.blueMoved
            home = self.blueHome
        elif color ==  "red":
            piece = self.red
            moved = self.redMoved
            home = self.redHome
        elif color ==  "green":
            piece = self.green
            moved = self.greenMoved
            home = self.greenHome
        elif color ==  "yellow":
            piece = self.yellow
            moved = self.yellowMoved
            home = self.yellowHome

        self.totalPieces = [self.blue, self.red, self.green, self.yellow]
        self.totalColor = ["blue", "red", "green", "yellow"]
        
        
        moving = Text(Point(700, 300), "Click on the piece \nyou wish to move " + str(n) + " spaces.")
        moving.setSize(10)
        moving.draw(self.win)

        while(done==False):
            p = self.win.getMouse()
            for pz in range(len(piece)):
                if (home[pz]==0 and(p.getX()-10) <= piece[pz].getCenter().getX()  and (p.getX()+10) >= piece[pz].getCenter().getX() and
                    (p.getY()-10) <=piece[pz].getCenter().getY() and (p.getY()+10) >= piece[pz].getCenter().getY()):
                    
                    ficha = piece[pz]
                    home = home[pz]
                    moved[pz]+=n
                    done=True
                    break

        while(n>0):
            time.sleep(0.25)
            #left Blue
            if (ficha.getCenter().getX()>= 219 and ficha.getCenter().getX()<= 273 and
                 ficha.getCenter().getY()>=50 and ficha.getCenter().getY()<= 212):
                ficha.move(0, 27)
                n-=1

            #bottom Red
            elif(ficha.getCenter().getX()>= 30 and ficha.getCenter().getX()<= 192 and
                 ficha.getCenter().getY()>=347 and ficha.getCenter().getY()<= 401):
                ficha.move(27, 0)
                n-=1
                
            #right green
            elif(ficha.getCenter().getX()>= 327 and ficha.getCenter().getX()<= 381 and
                 ficha.getCenter().getY()>=428 and ficha.getCenter().getY()<= 590):
                ficha.move(0, -27)
                n-=1
                
            #top yellow
            elif(ficha.getCenter().getX()>= 408 and ficha.getCenter().getX()<= 570 and
                 ficha.getCenter().getY()>=239 and ficha.getCenter().getY()<= 296):
                ficha.move(-27, 0)
                n-=1

            #top yellow corner
            elif(ficha.getCenter().getX()>= 381 and ficha.getCenter().getX()<= 408 and
                 ficha.getCenter().getY()>=239 and ficha.getCenter().getY()<= 293):
                ficha.move(-27, 27)
                n-=1
                
            #left Blue corner    
            elif(ficha.getCenter().getX()>= 219 and ficha.getCenter().getX()<= 273 and
                 ficha.getCenter().getY()>=212 and ficha.getCenter().getY()<= 239):
                ficha.move(27, 27)
                n-=1

            #bottom red corner
            elif(ficha.getCenter().getX()>= 192 and ficha.getCenter().getX()<= 219 and
                 ficha.getCenter().getY()>=347 and ficha.getCenter().getY()<= 401):
                ficha.move(27, -27)
                n-=1

            #right green corner
            elif(ficha.getCenter().getX()>= 327 and ficha.getCenter().getX()<= 381 and
                 ficha.getCenter().getY()>=401 and ficha.getCenter().getY()<= 428):
                ficha.move(-27, -27)
                n-=1

            #Center first upper-left    
            elif(ficha.getCenter().getX()>= 246 and ficha.getCenter().getX()<= 273 and
                 ficha.getCenter().getY()>=239 and ficha.getCenter().getY()<= 266):
                ficha.move(-27, 27)
                n-=1

            #Center first bottom-left
            elif(ficha.getCenter().getX()>= 219 and ficha.getCenter().getX()<= 246 and
                 ficha.getCenter().getY()>=347 and ficha.getCenter().getY()<= 374):
                ficha.move(27, 27)
                n-=1

            #Center first bottom-right
            elif(ficha.getCenter().getX()>= 327 and ficha.getCenter().getX()<= 354 and
                 ficha.getCenter().getY()>=374 and ficha.getCenter().getY()<= 401):
                ficha.move(27, -27)
                n-=1

            #Center first upper-right
            elif(ficha.getCenter().getX()>= 354 and ficha.getCenter().getX()<= 381 and
                 ficha.getCenter().getY()>=239 and ficha.getCenter().getY()<= 293):
                ficha.move(-27, -27)
                n-=1

            #Center second upper-left    
            elif(ficha.getCenter().getX()>= 219 and ficha.getCenter().getX()<= 246 and
                 ficha.getCenter().getY()>= 266 and ficha.getCenter().getY()<= 293):
                ficha.move(-27, 0)
                n-=1

            #Center second bottom-left
            elif(ficha.getCenter().getX()>= 246 and ficha.getCenter().getX()<= 273 and
                 ficha.getCenter().getY()>=374 and ficha.getCenter().getY()<= 401):
                ficha.move(0, 27)
                n-=1

            #Center second bottom-right
            elif(ficha.getCenter().getX()>= 354 and ficha.getCenter().getX()<= 381 and
                 ficha.getCenter().getY()>=347 and ficha.getCenter().getY()<= 374):
                ficha.move(27, 0)
                n-=1

            #Center second upper-right
            elif(ficha.getCenter().getX()>= 327 and ficha.getCenter().getX()<= 354 and
                 ficha.getCenter().getY()>=239 and ficha.getCenter().getY()<= 266):
                ficha.move(0, -27)
                n-=1

            #right Blue
            if (ficha.getCenter().getX()>= 327 and ficha.getCenter().getX()<= 381 and
                 ficha.getCenter().getY()>=77 and ficha.getCenter().getY()<= 239):
                ficha.move(0, -27)
                n-=1

            #top Red
            elif(ficha.getCenter().getX()>= 57 and ficha.getCenter().getX()<= 219 and
                 ficha.getCenter().getY()>=239 and ficha.getCenter().getY()<= 293):
                ficha.move(-27, 0)
                n-=1
                
            #left green
            elif(ficha.getCenter().getX()>= 219 and ficha.getCenter().getX()<= 273 and
                 ficha.getCenter().getY()>=401 and ficha.getCenter().getY()<= 563):
                ficha.move(0, 27)
                n-=1
                
            #bottom yellow
            elif(ficha.getCenter().getX()>= 381 and ficha.getCenter().getX()<= 543 and
                 ficha.getCenter().getY()>=347 and ficha.getCenter().getY()<= 401):
                ficha.move(27, 0)
                n-=1

            #Enter blue Home
            elif(moved[pz]>60 and ficha.getCenter().getX()>= 273 and ficha.getCenter().getX()<= 327 and
                 ficha.getCenter().getY()>=50 and ficha.getCenter().getY()<= 74):
                ficha.move(0, 27)
                n-=1
                
            #Enter red Home
            elif(moved[pz]>60 and ficha.getCenter().getX()>= 30 and ficha.getCenter().getX()<= 57 and
                 ficha.getCenter().getY()>=293 and ficha.getCenter().getY()<= 347):
                ficha.move(27, 0)
                n-=1
                
            #Enter green Home

            elif(moved[pz]>60 and ficha.getCenter().getX()>= 273 and ficha.getCenter().getX()<= 327 and
                 ficha.getCenter().getY()>=563 and ficha.getCenter().getY()<= 590):
                ficha.move(0, -27)
                n-=1
                
            #Enter yellow Home
            elif(moved[pz]>60 and ficha.getCenter().getX()>= 543 and ficha.getCenter().getX()<= 570 and
                 ficha.getCenter().getY()>=293 and ficha.getCenter().getY()<= 347):
                ficha.move(-27, 0)
                n-=1

            #left column
            elif(ficha.getCenter().getX()>= 30 and ficha.getCenter().getX()<= 57 and
                 ficha.getCenter().getY()>=239 and ficha.getCenter().getY()<= 347):
                ficha.move(0, 54)
                n-=1
                
            #top row
            elif(ficha.getCenter().getX()>= 273 and ficha.getCenter().getX()<= 381 and
                 ficha.getCenter().getY()>=50 and ficha.getCenter().getY()<= 74):
                ficha.move(-54, 0)
                n-=1

            #right column
            elif(ficha.getCenter().getX()>= 543 and ficha.getCenter().getX()<= 570 and
                 ficha.getCenter().getY()>=293 and ficha.getCenter().getY()<= 401):
                ficha.move(0, -54)
                n-=1

            #bottom row
            elif(ficha.getCenter().getX()>= 219 and ficha.getCenter().getX()<= 327 and
                 ficha.getCenter().getY()>=563 and ficha.getCenter().getY()<= 590):
                ficha.move(54, 0)
                n-=1
            #Home stretch Blue
            if (ficha.getCenter().getX()>= 273 and ficha.getCenter().getX()<= 327 and
                 ficha.getCenter().getY()>=77 and ficha.getCenter().getY()<= 266):
                ficha.move(0, 27)
                n-=1

            #Home stretch Red
            elif(ficha.getCenter().getX()>= 57 and ficha.getCenter().getX()<= 246 and
                 ficha.getCenter().getY()>=293 and ficha.getCenter().getY()<= 347):
                ficha.move(27, 0)
                n-=1
                
            #Home stretch green
            elif(ficha.getCenter().getX()>= 273 and ficha.getCenter().getX()<= 327 and
                 ficha.getCenter().getY()>=374 and ficha.getCenter().getY()<= 563):
                ficha.move(0, -27)
                n-=1
                
            #Home Stretch yellow
            elif(ficha.getCenter().getX()>= 354 and ficha.getCenter().getX()<= 543 and
                 ficha.getCenter().getY()>=293 and ficha.getCenter().getY()<= 347):
                ficha.move(-27, 0)
                n-=1

            #Home
            elif(ficha.getCenter().getX()>= 246 and ficha.getCenter().getX()<= 354 and
                 ficha.getCenter().getY()>=266 and ficha.getCenter().getY()<= 374):
                n=0
                reward = Text(Point(700, 350), "Home! " + color.capitalize() + " moves 10 spaces.")                  
                reward.setSize(10)
                reward.draw(self.win)
                time.sleep(1.5)
                reward.undraw()
                moving.undraw()
                self.move(color, 10)
                home=2
                
                

            
                
            

        for x in range(4):
            for y in range(4):
                if (ficha.getCenter().getX()-5<= self.totalPieces[x][y].getCenter().getX() and
                    ficha.getCenter().getY()-5<= self.totalPieces[x][y].getCenter().getY() and
                    ficha.getCenter().getX()+5>= self.totalPieces[x][y].getCenter().getX() and
                    ficha.getCenter().getY()+5>= self.totalPieces[x][y].getCenter().getY() and
                    color!=self.totalColor[x]):
                    
                    reward = Text(Point(700, 350), "Captured! " + color.capitalize() + " moves 20 spaces.")
                    self.captured(self.totalColor[x], y)                    
                    reward.setSize(10)
                    reward.draw(self.win)
                    time.sleep(1.5)
                    reward.undraw()
                    moving.undraw()
                    self.move(color, 20)
                
        try:
            moving.undraw()
        except:
            print("Already undrawn")
        
        
        
    def createDice(self, center, size):
        center.move(-3*size,0)
        self.dice = []
        for i in range(2):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def turn(self, n):
        players = self.players
        turn = n%4
        if turn ==0:
            players[0].undraw()
            players[0].setFill("blue")
            players[0].draw(self.win)
            

            players[3].undraw()
            players[3].setFill("black")
            players[3].draw(self.win)

            return "blue"
        elif turn ==1:
            players[1].undraw()
            players[1].setFill("gold")
            players[1].draw(self.win)
            

            players[0].undraw()
            players[0].setFill("black")
            players[0].draw(self.win)

            return "yellow"
        elif turn ==2:
            players[2].undraw()
            players[2].setFill("green")
            players[2].draw(self.win)
            

            players[1].undraw()
            players[1].setFill("black")
            players[1].draw(self.win)
            
            return "green"
        else:
            players[3].undraw()
            players[3].setFill("red")
            players[3].draw(self.win)
            

            players[2].undraw()
            players[2].setFill("black")
            players[2].draw(self.win)

            return "red"
    

    
            
    def setDice(self, values):
        for i in range(2):
            self.dice[i].setValue(values[i])


    def close(self):
        self.win.close()

        

class Parcheesi:

    def __init__(self, interface):
        self.interface = interface
        self.dice = Dice()
        self.spaces = [0]*68
        self.over = False
        self.interface.createPieces()

    
        
    def run(self):
        n = 0
        while(self.over!=True):
            piece = self.interface.turn(n)

            if piece == "blue":
                Home = self.interface.blueHome
            elif piece =="green":
                Home = self.interface.greenHome
            elif piece == "red":
                Home = self.interface.redHome
            elif piece == "yellow":
                Home = self.interface.yellowHome
                
            
            key = self.interface.win.getKey()
            if (key == "Escape"):
                self.over = True
                
            elif (key == "r"):
                
                self.moves = []
                self.dice.roll()
                self.interface.setDice(self.dice.values())
                Sum = 0
                for i in self.dice.score():
                    Sum +=i
                    if i ==5:
                        self.interface.start(piece)                    
                    else:
                        if Sum ==5:
                            self.interface.start(piece)
                            self.moves = []
                        else:
                            self.moves.append(i)
                            if(len(self.moves)>1 and self.moves[0]==self.moves[1]):
                                n-=1
                                doubles = Text(Point(700, 400), "Doubles! " + piece.capitalize() + " rolls again.\nTwo additional rolls awarded\nTotal: 14 spaces")
                                doubles.setSize(10)
                                doubles.draw(self.interface.win)
                                time.sleep(1.5)
                                doubles.undraw()
                                self.moves.append(7-self.moves[0])
                                self.moves.append(7-self.moves[1])
                    
                
                for l in range(4):
                    if Home[l]==0:                        
                        while(len(self.moves)!=0):
                            print(self.moves)
                            size = len(self.moves)-1
                            self.interface.move(piece, self.moves[size])
                            self.moves.pop(size)
                        break
                if Home[0] ==2 and Home[1]==2 and Home[2]==2 and Home[3]==2:
                    Over = Text(Point(700, 400), "Game Over! " + piece.capitalize() + " won.")
                    Over.setSize(10)
                    OVer.draw(self.interface.win)
                    time.sleep(5)
                    Over.undraw()
                    self.over = True
                    
                        
            
            n += 1
            time.sleep(1)
            
        self.interface.close()   
            
        



def main():
    graph = GraphicInterface()

    game = Parcheesi(graph)
    game.run()


main()

