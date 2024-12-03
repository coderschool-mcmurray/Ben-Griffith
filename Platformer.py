import pygame
import time

#initializing starting Global variables
WINDSIZE=[500,500]
COLORS={
    'RED' : (255,0,0),
    'GREEN' : (0,255,0),
    'BLUE' : (0,0,255),
    'WHITE' : (255,255,255),
    'BLACK' : (0,0,0),
    'PURPLE' : (134,4,199),
    'GRAY' : (50,50,50)}
GRAVITY=0.75

#it is the jumping things that makes stuuf happy
fall=0
jump=-9.5
startJump=jump

#starting location
x = 0
y = 0

#character size
w = 10
l = 10

#character speed
speed = 5
default_speed = 5
blue_speed = 2
time_for_speed = 0

#rando variables
delete=[]
key=False
move_l = False
move_r = False
j = False

#game running? level?
r = True
level = 1

#initalizing pygame
pygame.init()
pygame.display.set_caption('The Best Platformer That May Or May Not Be Possible')
display = pygame.display.set_mode(WINDSIZE)

#create floor, wall and everything in between class
class Block:
    x_loc=0
    y_loc=0
    length=0
    width=0
    color=(0,0,0)
    def __init__(self, x_loc=0, y_loc=0, length=0, width=0, color='RED'):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.length = length
        self.width = width
        self.color = color
    def draw(self, display):
        pygame.draw.rect(display,COLORS[self.color],(self.x_loc,self.y_loc,self.width,self.length))
    def is_collision(self,x,y,l,w):
        #detects if blocks are outside of each other
        if x>=self.x_loc + self.width or x+w<=self.x_loc:
            return False
        if y>=self.y_loc + self.length or y+l<=self.y_loc:
            return False
        return True

#gets the level and returns a list of all of the blocks in the level
def get_level(workfile):
    blocks = []
    f = open(workfile, 'r', encoding="utf-8")
    for line in f:
        line = line.split(',')
        x = int(line[0])
        y = int(line[1])
        length = int(line[2])
        width = int(line[3])
        color = line[4]
        blocks.append(Block(x,y,length,width,color))
    return blocks

# use the get level function
blocks = get_level(f'level{level}')
b_blocks=list(blocks)

#gets the purple and grey blocks locations and puts them in decending order
for i,b in enumerate(blocks):
    if b.color=='GRAY':
        delete.append(i)
    if b.color=='PURPLE':
        delete.append(i)
delete.reverse()

while r:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
    move_l = True
    move_r = True
    j = False
    
    #speed beign set back to normal speed 1 sec after gettign off of the blue block
    if int(time.time() * 1000) >= time_for_speed:
        speed = default_speed
    
    for b in blocks:
        #if we are standing on the block- we can jump
        if b.is_collision(x,y+1,l,w):
            j = True
            #slows us down if we are on blue
            if b.color == "BLUE":
                time_for_speed = int(time.time()*1000)+1000
                speed = blue_speed
        #see if we are hitting a wall to the left
        if b.is_collision(x-speed,y,l,w):
            move_l = False
            #white mneans climb
            if b.color == "WHITE":
                j = True
            if b.color== "PURPLE":
                move_l = True
        if b.is_collision(x+speed,y,l,w):
            move_r = False
            if b.color == "WHITE":
                j = True
            if b.color== "PURPLE":
                move_r = True
    keys=pygame.key.get_pressed()
    #you can't jump above the map alos allows jumping
    if keys[pygame.K_UP] and y > 0 and j:
        fall = jump
    #moves left unless hitting a boundary
    if keys[pygame.K_LEFT] and x > 0 and move_l:
        x -= speed
    #moves right ynless hitting boundary
    if move_r and keys[pygame.K_RIGHT] and x < WINDSIZE[0]-w:
        x += speed
    #if 1 is pressed exit teh game
    if keys[pygame.K_1]:
        r = False
    #Falling and rising until hitting black block
    fall += GRAVITY
    ex = False
    if fall > 0:
        for _ in range(round(fall)):
            y += 1
            for b in blocks:
                if b.is_collision(x,y,l,w):
                    if b.color == "BLACK":
                        ex = True
                        break
            if ex:
                break
    else:
        for _ in range(round(abs(fall))):
            y -= 1
            for b in blocks:
                if b.is_collision(x,y,l,w):
                    if b.color == "BLACK":
                        ex = True
                        break
            if ex:
                break
    # Allows movement to next level
    if y > WINDSIZE[1]:
        blocks.clear()
        level += 1
        blocks = get_level(f'level{level}')
        x = 0
        y = 0
        fall = 0
        b_blocks=list(blocks)
        delete.clear()
        for i,b in enumerate(blocks):
            if b.color=='GRAY':
                delete.append(i)
            if b.color=='PURPLE':
                delete.append(i)
        delete.reverse()

    
    for b in blocks:
        if b.is_collision(x,y,l,w):
            #return jump power to og
            jump = startJump
            #death
            if b.color == "RED":
                x = 0
                y = 0
                blocks=b_blocks
            #is key for grey
            elif b.color =='PURPLE':
                   key=True
            #mega jump if on green
            elif b.color == 'GREEN':
                jump = -25
            #stop rising
            elif fall < 0:
                y = b.y_loc + b.length
            else:
                y = b.y_loc-l
            fall = 0
    #purple deletes gray and itself
    if key:
        for i in delete:
            blocks.pop(i)
        key = False
    #draw game
    display.fill((100,100,100))
    for b in blocks:
        b.draw(display)
    pygame.draw.rect(display,COLORS['BLUE'],(x,y,w,l))
    pygame.display.update()

pygame.quit()
quit()