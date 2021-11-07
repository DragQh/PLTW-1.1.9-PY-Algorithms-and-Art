#   a114_nested_loops_4.py
import turtle as trtl
import random
from random import randint

# Selecting your shape
Shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
YourShape = ''
while YourShape not in Shapes:
  YourShape = input('What shape would you like? (arrow, turtle, circle, square, triangle, classic, or random?)')
  RandomShape = False
  if YourShape == 'random':
    RandomShape = True
    YourShape = random.choice(Shapes)
  else:
    pass
# Choosing the color
colors = ['black']
Letters = 'abcdef1234567890' # Letters able to be used as a hex code
# puts letters into seperate lists
UseableLetters = []
for i in Letters:
  UseableLetters.append(i)
# Choose random hex code  
def NewColor():
  ColorCode = '#'
  for n in range (1, 7):
    rand = randint(0, 15)
    for letter in UseableLetters:
      if UseableLetters.index(letter) == rand:
        ColorCode += letter
  if ColorCode not in colors:
    colors.append(ColorCode)
  else:
    NewColor = False   
  return ColorCode  

# Creating stamp
STurtle = trtl.Turtle(shape=YourShape)
STurtle.stamp()
NextColor = True
sizes = 1.00
STurtle.speed('fast')
# Countinuely creates shapes
while NextColor:
  if RandomShape: # Looks if user chose random, then chooses random shapes
    YourShape = random.choice(Shapes)
    STurtle = trtl.Turtle(shape=YourShape)
  STurtle.turtlesize(sizes)
  STurtle.right(randint(1, 360)) # Turns a random direction
  STurtle.color(NewColor()) # Calls NewColor function
  STurtle.penup()
  STurtle.goto(randint(-250, 250), randint(-250, 250)) # Got to random postion
  STurtle.pendown()
  STurtle.stamp()
  STurtle.turtlesize(sizes)
  if sizes >= 5:
    sizes = 1
  else:  
    sizes += 0.05



 
wn = trtl.Screen()
wn.mainloop()
