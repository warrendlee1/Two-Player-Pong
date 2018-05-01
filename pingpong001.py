"""
AP CSP Create Task: Two-Player Pong Game
"""

from graphics import *
from random import *

# height and width of game's window in pixels
HEIGHT = 400
WIDTH = 700

# radius of ball in pixels
RADIUS = 10

# size of paddle in pixels
PADWIDTH = 10
PADHT = 50

# instantiate window and choose background color
screen = GraphWin("2 Player Pong", WIDTH, HEIGHT)
colors = ["Light Gray", "Green", "White", "Gold", "Aquamarine", "Light Pink", "Tan"]
for i in colors:
    print(i)
choose = str(input("Background color: "))
while choose not in colors:
    choose = str(input("Background color: "))
screen.setBackground(choose)
screen.getMouse()

#parent function
def main():
    #instantiate ball
    ball = initBall()
    #instantiate paddle 1
    pad1 = initPaddle1()
    #instantiate paddle 2
    pad2 = initPaddle2()
    #instantiate scoreboard, centered in middle of window
    label = initScoreboard()
    #initiate score
    score = 0
    #create text for game over
    gg = "GAME OVER"

    # initial velocity
    xvelocity = 3
    yvelocity = (random() * 5 + 0.02)

    #when mouse clicked
    screen.getMouse()

    while True:
        #move ball
        ball.move(xvelocity, yvelocity)

        # moves the paddles
        padMove(pad1, pad2)

        # get (x,y) of the ball
        centerBall = ball.getCenter()
        xBall = centerBall.getX()
        yBall = centerBall.getY()

        # bounce off edge of window
        if checkTop(yBall):
            yvelocity = -yvelocity

        # checks if the paddles hit the ball
        if padHit(pad1, pad2, xBall, yBall):
            pad1.setFill("red")
            pad2.setFill("blue")
            score += 1
            xvelocity = -xvelocity
            updateScoreboard(label, score)
        # ends game when the ball hits the sides
        if checkSides(xBall):
            gameover(label,gg,ball,screen)
            exit(0)

#separate child functions
def initScoreboard():
   x = WIDTH / 2
   y = HEIGHT / 4
   anchorPoint = Point(x, y)
   label = Text(anchorPoint, "0")
   label.setSize(36)
   label.setTextColor("Dark Gray")
   label.draw(screen)
   return label

def initBall():
   center = Point(350, 200)
   ball = Circle(center, RADIUS)
   ball.setFill("black")
   ball.draw(screen)
   return ball

def initPaddle1():
    paddle = Rectangle(Point(100,175), Point(100+PADWIDTH,175+PADHT))
    paddle.setFill("red")
    paddle.draw(screen)
    return paddle

def initPaddle2():
    paddle = Rectangle(Point(600,175), Point(600-PADWIDTH,175+PADHT))
    paddle.setFill("blue")
    paddle.draw(screen)
    return paddle

def padMove(pad1,pad2):
    #sets up the different vars
    user_event = screen.checkKey()
    padPt1 = pad1.getP1()
    padY1 = padPt1.getY()
    padPt2 = pad2.getP1()
    padY2 = padPt2.getY()

    #movement for pad1
    if user_event == "w" and padY1 > 0:
        pad1.move(0, -20)
    elif user_event == "s" and padY1 + PADHT < HEIGHT:
        pad1.move(0, 20)
    #movement for pad2
    if user_event == "Up" and padY2 > 0:
        pad2.move(0, -20)
    elif user_event == "Down" and padY2 + PADHT < HEIGHT:
        pad2.move(0, 20)

def padHit(pad1, pad2, xBall, yBall):
    pointPaddle1 = pad1.getP1()
    xPaddle1 = pointPaddle1.getX()
    yPaddle1 = pointPaddle1.getY()
    pointPaddle2 = pad2.getP1()
    xPaddle2 = pointPaddle2.getX()
    yPaddle2 = pointPaddle2.getY()
    if (xBall + RADIUS >= xPaddle1 and
        xBall - RADIUS <= (xPaddle1 + PADWIDTH)
        and yPaddle1 - yBall < 0 and yPaddle1 - yBall > -50
        ):
        pad1.setFill("green")
        return True

    elif (xBall + RADIUS >= xPaddle2 - PADWIDTH and
          xBall + RADIUS <= (xPaddle2 + PADWIDTH)
          and yPaddle2 - yBall < 0 and yPaddle2 - yBall > -50
        ):
       pad2.setFill("green")
       return True

    else:
        return False

def checkTop(yBall):
    while (yBall < 0 or yBall > 400):
        return True
    return False

def checkSides(xBall):
    while(xBall < 0 or xBall > 700):
        time.sleep(0.5)
        return True
    return False

def updateScoreboard(label, score):
    label.setText(score)
    return label

def gameover(label,gg,ball,screen):
    ball.undraw()
    label.setTextColor("Red")
    label.setText(gg)
    time.sleep(1)
    screen.close()
    return label

if __name__ == "__main__":
   main()