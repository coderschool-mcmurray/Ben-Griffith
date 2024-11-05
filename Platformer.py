import pygame


WINDSIZE=[500,500]
COLORS={
    'RED' : (255,0,0),
    'GREEN' : (0,255,0),
    'BLUE' : (0,0,255),
    'WHITE' : (255,255,255),
    'BLACK'  :(0,0,0),
    'GRAY' : (50,50,50)}

GRAVITY=0.75
fall=0
jump=-9.5
startJump=-9.5
pygame.init()

pygame.display.set_caption('The Best Platformer That May Or May Not Be Possible')
display = pygame.display.set_mode(WINDSIZE)

#create floor class
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
        color=line[4]
        blocks.append(Block(x,y,length,width,color))
    return blocks
#starting location
x = 0
y= 0

#character size
w= 10
l= 10

#character speed
speed = 5

#game running?
r = True
level=7
blocks=get_level(f'level{level}')

move_l=False
move_r=False
j=False
while r:
    pygame.time.delay(20)
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
            x=b.x_loc+b.width
            if b.color=="WHITE":
                j=True
        if b.is_collision(x+speed,y,l,w):
            move_r=False
            x=b.x_loc-w
            if b.color=="WHITE":
                j=True
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
    ex=False
    if fall>0:
        for _ in range(round(fall)):
            y+=1
            for b in blocks:
                if b.is_collision(x,y,l,w):
                    if b.color == "BLACK":
                        ex=True
                        break
            if ex:
                break
    else:
        y+=fall
    if y>WINDSIZE[1]:
        blocks.clear()
        level+=1
        blocks=get_level(f'level{level}')
        x=0
        y=0
        fall=0
    for b in blocks:
        if b.is_collision(x,y,l,w):
            jump = startJump
            if b.color=="RED":
                x=0
                y=0
            elif b.color=='GREEN':
                jump=-25
            elif fall<0:
                y=b.y_loc+ b.length
            else:
                y=b.y_loc-l
            fall=0
    display.fill((100,100,100))
    for b in blocks:
        b.draw(display)
    pygame.draw.rect(display,COLORS['BLUE'],(x,y,w,l))
    pygame.display.update()

pygame.quit()
quit()