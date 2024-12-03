'''
s-save level
l-load level
M click- delete the clicked block on the lowest layer
0-Red (stranger danger)
1- Green (Jump Ooze)
2-Blue(slow)
3-white(wall Jump)
4-Black(normal)
5- Gray(door)
6- Purple(key)
r-undo
'''
import pygame


WINDSIZE=[600,600]
##This is how the diferent colors are made##
COLORS={
    'RED' : (255,0,0),
    'GREEN' : (0,255,0),
    'BLUE' : (0,0,255),
    'WHITE' : (255,255,255),
    'BLACK'  :(0,0,0),
    'PURPLE' :(134,4,199),
    'GRAY' : (50,50,50)}

pygame.init()

pygame.display.set_caption('level maker')
display = pygame.display.set_mode(WINDSIZE)
##This is how the blocks are created##
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

##This is where the level is saved##
def save(writefile,blocks):
    f =open(writefile,'w')
    for block in blocks:
        f.write(f"{block.x_loc-50},{block.y_loc-50},{block.length},{block.width},{block.color},\n")
    f.close()

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
        blocks.append(Block(x+50,y+50,length,width,color))
    return blocks

r=True

create=False

x=0
y=0
color='WHITE'


blocks=[]
##This is how the blocks are in the game and what the different colors##
while r:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r= False
        elif event.type==pygame.MOUSEBUTTONUP:
            x_pos,y_pos=pygame.mouse.get_pos()
            if create:
                if x_pos>x and y_pos>y:
                    blocks.append(Block(x,y,y_pos-y,x_pos-x,color))
                create=False
            else:
                if len(blocks)==0:
                    x=x_pos
                    y=y_pos
                    create=True
                for i in range(len(blocks)):
                    keys=pygame.key.get_pressed()
                    if blocks[i].is_collision(x_pos,y_pos,1,1) and keys[pygame.K_m]:
                        blocks.pop(i)
                        break
                else:
                    x=x_pos
                    y=y_pos
                    create=True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_s]:
        level=input()
        save(level,blocks)
    elif keys[pygame.K_l]:
        blocks = get_level(input())
    elif keys[pygame.K_0]:
        color="RED"
    elif keys[pygame.K_1]:
        color="GREEN"
    elif keys[pygame.K_2]:
        color="BLUE"
    elif keys[pygame.K_3]:
        color="WHITE"
    elif keys[pygame.K_4]:
        color="BLACK"
    elif keys[pygame.K_5]:
        color="GRAY"
    elif keys[pygame.K_6]:
        color='PURPLE'
    elif keys[pygame.K_r]:
        blocks.pop(-1)
        pygame.time.delay(100)
#This is the color of the base color of the Game
    display.fill((30,30,30))
    pygame.draw.rect(display,(100,100,100),(50,50,500,500))
    for b in blocks:
        b.draw(display)
    pygame.display.update()
#This is how the game quits
pygame.quit()
quit()