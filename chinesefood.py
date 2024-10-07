import pygame


WINDSIZE=[600,600]
##This is how the diferent colors are made##
COLORS={
    'RED' : (255,0,0),
    'GREEN' : (0,255,0),
    'BLUE' : (0,0,255),
    'WHITE' : (255,255,255),
    'BLACK'  :(0,0,0),
    'GRAY' : (10,10,10)}

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
        f.write(f"{block.x_loc-50},{block.y_loc-50},{block.length-50},{block.width-50},{block.color},\n")
    f.close()

r=True

create=False

x=0
y=0
color='WHITE'


blocks=[]
##This is how the blocks are in the game and what the different colors##
while r:
    pygame.time.delay(10)
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
                    
                    if blocks[i].is_collision(x_pos,y_pos,1,1):
                        blocks.pop(i)
                        break
                else:
                    x=x_pos
                    y=y_pos
                    create=True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_s]:
        save('test_level',blocks)
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
#This is the color of the base color of the Game
    display.fill(COLORS['GRAY'])
    pygame.draw.rect(display,(100,100,100),(50,50,500,500))
    for b in blocks:
        b.draw(display)
    pygame.display.update()
#This is how the game quits
pygame.quit()
quit()