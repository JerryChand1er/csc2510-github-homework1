# Main.py
# Originally created by Brandon Vandergriff
# Ruined by: Wesley Ni
# Ruined by: Fenil Patel
# Ruined by: Ethan Gentry
# Ruined by: Cristian Rocha
# Ruined by: Ivette Garcia
# Ruined by: Brandon Soto
# Ruined by: Vincent Pestilli
# Ruined by: Jerry Chandler
# Ruined by: Elliot Stewart
# Ruined by: teagan tobias

import random
import turtle
import time



def funcRocha():
    quotes = [
        "If strength is your virtue, then what are you without it?",
        "You seek answers, but have you yet questioned the question?",
        "If knowledge is power, why do the wise feel so powerless?",
        "You ask me for guidance, but can a man be guided who does not know he is lost?",
        "If certainty is your comfort, what will you do when doubt arrives?",
        "The unexamined life is not worth living — so why do you avoid the mirror?",
        "If love is your anchor, what happens when the sea dries up?",
        "You think you know, but do you know that you know nothing?",
        "If time is your enemy, why do you waste it asking a program for wisdom?",
        "True wisdom begins when you realize this 8-Ball knows more than you.",
    ]
    print("The Socratic 8-Ball has spoken:")
    print(f'  "{random.choice(quotes)}"')



def funcStewart():
    print("what is your favorite number 1 - 5")
    coolness_number = int(input("Pick a number from 1 to 5: "))

    if coolness_number == 1:
        print("1 is a basic number and not very cool")
    elif coolness_number == 2:
        print("2 is a very cool number its nice in math and is my favorite")
    elif coolness_number == 3:
        print("3 is not a coll number and is ugly!")
    elif coolness_number == 4:
        print("4 is a cool number and it looks nice.")
    elif coolness_number == 5:
        print("5 you picked it because it is a big number but big numbers are cool!")
    else:
        print("Invalid choice. Pick a number between 1 and 5.")

def funcVandergriff():
    print("")


def funcGarcia():
    number = int(input("Want to hear a joke? Enter 1 for yes and 2 for no: "))

    if number == 1:
        print("Joke failed to load")
      
    elif number == 2:
        print("You're mean")
      
    else:
        print("You don't deserve to hear a joke if you can't even type 1 or 2")
    

def funcWells():
    for i in range(4):
        print("Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy.")


def funcNi():
  print(r"""
 _____
< Cow >
 -----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
  """)


def funcPatel():
    print("Tigers are awesome.")


def funcGentry():
    print("Check out this awesome fish: ")
    print("><(((*>")
    print("Isn't he awesome?")

#May require you to pip install pyjokes
import pyjokes

def funcPestilli():
    jokesNum = int(input("How many jokes would you like? \n> "))
    while (jokesNum > 0):
      print(pyjokes.get_joke())
      jokesNum -= 1


def funcSoto():
    names = ["Ironclad", "Silent", "Regeant", "Necrobinder", "Defect"]
    number = random.randint(1, 5)

    print(f"Choose This Character: {names[number -1]}")


def funcIsmail():

    # horse
    # r means raw string btw
    print(r"Hey, I am Ismail")
# Ruined by: John Miller

import time
import urllib.request

def funcChandler():
  import turtle
  import time
  import random

  delay = 0.1

  #score
  score = 0
  high_score = 0

  #set up screen
  wn = turtle.Screen()
  wn.title("Snake Game")
  wn.bgcolor("green")
  wn.setup(width=600, height=600)
  wn.tracer(0) #turns off the screen updates

  #snake head
  head = turtle.Turtle()
  head.speed(0)
  head.shape("square")
  head.color("black")
  head.penup()
  head.goto(0,0)
  head.direction = "stop"

  #snake food
  food = turtle.Turtle()
  food.speed(0)
  food.shape("circle")
  food.color("red")
  food.penup()
  food.goto(0,100)

  segments = []

  #pen
  pen = turtle.Turtle()
  pen.speed(0)
  pen.shape("square")
  pen.color("white")
  pen.penup()
  pen.hideturtle()
  pen.goto(0,260)
  pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

  #functions to move the snake
  def go_up():
      if head.direction != "down":
          head.direction = "up"

  def go_down():
      if head.direction != "up":
          head.direction = "down"

  def go_right():
      if head.direction != "left":
          head.direction = "right"

  def go_left():
      if head.direction != "right":
          head.direction = "left"

  def move():
      x = head.xcor()
      y = head.ycor()
      if head.direction == "up":
          head.sety(y + 20)
      elif head.direction == "down":
          head.sety(y - 20)
      elif head.direction == "right":
          head.setx(x + 20)
      elif head.direction == "left":
          head.setx(x - 20)

  #keyboard bindings
  wn.listen()
  wn.onkeypress(go_up, "Up")
  wn.onkeypress(go_down, "Down")
  wn.onkeypress(go_right, "Right")
  wn.onkeypress(go_left, "Left")
  wn.onkeypress(go_up, "w")
  wn.onkeypress(go_down, "s")
  wn.onkeypress(go_right, "d")
  wn.onkeypress(go_left, "a")

  #main game loop
  running = True
  while running:
      wn.update()

      #check for collision with border
      if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
          time.sleep(1)
          head.goto(0,0)
          head.direction = "stop"
          running = False
          break

      #check for collision with food
      if head.distance(food) < 20:
          
          #move food to random spot
          x = random.randint(-290,290)
          y = random.randint(-290,270)
          food.goto(x,y)

          #add a segment
          new_segment = turtle.Turtle()
          new_segment.speed(0)
          new_segment.shape("circle")
          new_segment.color("black")
          new_segment.penup()
          segments.append(new_segment)

          #shorten delay
          delay -= 0.001

          #increase score
          score += 10

          if score > high_score:
              high_score = score
          
          pen.clear()
          pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

      # move the end segments first in reverse order
      for index in range(len(segments)-1, 0, -1):
          x = segments[index-1].xcor()
          y = segments[index-1].ycor()
          segments[index].goto(x,y)

      #move segment 0 to where the head is
      if len(segments) > 0:
          x = head.xcor()
          y = head.ycor()
          segments[0].goto(x,y)

      move()

      #check for head collison with body segments
      for segment in segments:
          if segment.distance(head) < 20:
              time.sleep(1)
              head.goto(0,0)
              head.direction = "stop"
              running = False
              break
          
      time.sleep(delay)

  wn.bye()



def funcJones():
    print("This my function now!")

def fightClub(): 
    print("rule 1: you do not talk about fight club.")
    print("rule 2: you DO NOT talk about fight club.")
    print("rule 3: if some yells stop, goes limp, or taps out, the fight is over.")
    print("rule 4: only two fighters to a fight.")
    print("rule 5: one fight at a time.")
    print("rule 6: no shirts, no shoes.")
    print("rule 7 : fights will go on as long as they have to.")
    print("rule 8: if this is your first night at fight club, you have to fight.")

def updateProgressBarJohnMiller(percent):
  bar_length = 25  # should be less than 100
  print('\r', end="", flush=True)
  print("Downloading Bee Movie Script: [{:{}}] {:>3}%".format('■'*int(percent/(100.0/bar_length)), bar_length, int(percent)), end="", flush=True)

def funcJohnHMiller():
  data =  urllib.request.urlopen("https://git.lysator.liu.se/catears/beemovie/-/raw/master/beemovie.txt")
  with open("beeMovieScript.txt", 'w') as writeFile:
    total = 4563  # total line count
    currentLine = 1    
    for line in data:
      lineText = str(line)
      lineText = lineText[2:len(lineText)-3]+"\n"
      writeFile.write(lineText)

      updateProgressBarJohnMiller(100.0*currentLine/total)
      currentLine = currentLine + 1

      time.sleep(0.002)
    updateProgressBarJohnMiller(100.0)
  print("\nScript sucessfully downloaded")
  
def funcTobias():
    print("hi im teags and i like sharks. bye")

if __name__ == "__main__":
    funcStewart()
    funcVandergriff()
    funcPatel()
    funcRocha()
    funcPestilli()
    funcGentry()
    funcGarcia()
    funcSoto()
    funcIsmail()
    funcChandler()
    funcJohnHMiller()
    funcJones()
    fightClub()
    funcTobias()