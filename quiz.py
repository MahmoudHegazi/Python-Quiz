import turtle
import time

def square():
	amy = turtle.Turtle()
	amy.color("blue")
	amy.width(10)
	amy.speed(2)
	for side in range(4):
		amy.forward(100)
		amy.left(90)
	amy.ht()

def clean_square():
	amy = turtle.Turtle()
	amy.color("white")
	amy.width(10)
	amy.speed(0)
	for side in range(4):
		amy.forward(100)
		amy.left(90)
	amy.ht()
	
def circle():
    amy = turtle.Turtle()
    amy.color("lightblue")
    amy.width(10)
    amy.speed(2)
    for side in range(100):
        amy.forward(2)
        amy.left(2)
    amy.ht()

def clean_circle():
    amy = turtle.Turtle()
    amy.color("white")
    amy.width(10)
    amy.speed(0)
    for side in range(100):
        amy.forward(2)
        amy.left(2)
    amy.ht()    



def right():
    amy = turtle.Turtle()
    amy.color("green")
    amy.width(10)
    amy.left(115)
    amy.forward(30)
    amy.back(30)
    amy.right(115)
    amy.left(50)
    amy.forward(70)
    amy.ht()

def clean_right():
    amy = turtle.Turtle()
    amy.color("white")
    amy.width(10)
    amy.left(115)
    amy.forward(30)
    amy.back(30)
    amy.right(115)
    amy.left(50)
    amy.forward(70)
    amy.ht()    


def wrong():
    amy = turtle.Turtle()
    amy.color("red")
    amy.width(10)
    amy.left(50)
    amy.forward(30)
    amy.back(60)
    amy.forward(30)
    amy.left(80)
    amy.forward(30)
    amy.back(60)
    amy.ht()

def clean_wrong():
    amy = turtle.Turtle()
    amy.color("white")
    amy.width(10)
    amy.left(50)
    amy.forward(30)
    amy.back(60)
    amy.forward(30)
    amy.left(80)
    amy.forward(30)
    amy.back(60)
    amy.ht()    

def quiz():
    score = 0
    ans = ["10", "n", "n", "turtle", "n", "lightblue"]
    name = str(input("Please Can You Tell me Your Name"))
    qs1 = str(input("5 + 5 = ?"))
    print(" ")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    qs2 = str(input("int type in python refred to international ?(y/n)"))
    print(" ")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    qs3 = str(input("java and savascript are used for same propuse ?(y/n)"))
    print(" ")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    square()
    qs4 = str(input("what is the name of this library which used draw shapes in python ?"))
    print(" ")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    clean_square()    
    qs5 = str(input("HTML referes to 'Hyper transfer markup languages' ? (y/n)"))   
    circle()
    print(" ")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    qs6 = str(input("What is the color name of the circle ?"))
    clean_circle()
    print(" ")
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    
    if qs1 == ans[0]:
        score += 1
    else:
        score += 0
        
    if qs2 == ans[1]:
        score += 1
    else:
        score += 0
        
    if qs3 == ans[2]:
        score += 1
    else:
        score += 0
        
    if qs4 == ans[3]:
        score += 1
    else:
        score += 0
        
    if qs5 == ans[4]:
        score += 1
    else:
        score += 0
        
    if qs6 == ans[5]:
        score += 1
    else:
        score += 0
    print("congratulations Mr " + str(name) + " You Have got: " + str(score))    
    if int(score) > 3:
        print("You got score hight than 3 good job")
        right()
        time.sleep(10)
        clean_right
    else:
        print("You got less than 3 right answers try again")
        wrong()
        time.sleep(10)
        clean_wrong
    renew = str(input("Do you Want Try Quiz Again (y/n) ?"))
    if renew == "y" or renew == "yes":
        quiz()
    else:
        return("thanks for you this Quiz Applaction")
quiz()
 
            
    
