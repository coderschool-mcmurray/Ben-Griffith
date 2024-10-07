import pygame


WINDSIZE=[500,500]
COLORS={
    'RED' : (255,0,0),
    'GREEN' : (0,255,0),
    'BLUE' : (0,0,255),
    'WHITE' : (255,255,255),
    'BLACK'  :(0,0,0),
    'GRAY' : (10,10,10)}

GRAVITY=1
fall=0
jump=-15
pygame.init()

pygame.display.set_caption('Dot Game thingy')
display = pygame.display.set_mode(WINDSIZE)

#create floor class
class Block:
    x_loc=0
    y_loc=0
    length=0
    width=0
    color=(0,0,0)
    def __init__(self, x_loc=0, y_loc=0, length=0, width=0, color=COLORS['RED']):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.length = length
        self.width = width
        self.color = color
    def draw(self, display):
        pygame.draw.rect(display,self.color,(self.x_loc,self.y_loc,self.width,self.length))
    def is_collision(self,x,y,l,w):

        if x>=self.x_loc + self.width or x+w<=self.x_loc:
            return False
        if y>=self.y_loc + self.length or y+l<=self.y_loc:
            return False
        return True

def get_level(workfile):
    blocks=[]
    f=open(workfile, 'r', encoding="utf-8")
    for line in f:
        line=line.split(',')
        x=int(line[0])
        y=int(line[1])
        length=int(line[2])
        width=int(line[3])
        color=COLORS[line[4]]
        blocks.append(Block(x,y,length,width,color))
    return blocks
#starting location
x = 40
y= 70

#character size
w= 10
l= 10

#character speed
speed = 5

#game running?
r = True
blocks=get_level('level1')

move_l=False
move_r=False
j=False
while r:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r= False
    move_l=True
    move_r=True
    j=False
    
    for b in blocks:
        if b.is_collision(x,y+1,l,w):
            j=True
        if b.is_collision(x-speed,y,l,w):
            move_l=False
        if b.is_collision(x+speed,y,l,w):
            move_r=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and y>0 and j:
        fall=jump
    if keys[pygame.K_LEFT] and x>0 and move_l:
        x-=speed
    if move_r and keys[pygame.K_RIGHT] and x<WINDSIZE[0]-w:
        x+=speed
    if keys[pygame.K_1]:
        r=False
    fall+=GRAVITY
    y+=fall
    for b in blocks:
        if b.is_collision(x,y,l,w):
            if fall<0:
                y=b.y_loc+ b.length
            else:
                y=b.y_loc-l
            fall=0
    display.fill(COLORS['GRAY'])
    for b in blocks:
        b.draw(display)
    pygame.draw.rect(display,COLORS['BLUE'],(x,y,w,l))
    pygame.display.update()

pygame.quit()
quit()