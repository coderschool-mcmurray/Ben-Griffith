import pygame

windsize=[500,500]
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

pygame.init()

pygame.display.set_caption('Dot Game thingy')
display = pygame.display.set_mode(windsize)

#starting location
x = 40
y= 70

#character size
w= 10
l= 10

#character speed
speed = 2

#game running?
r= True

while r:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.quit:
            r= False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]and y>0:
        y-=speed
    if keys[pygame.K_LEFT]and x>0:
        x-=speed
    if keys[pygame.K_DOWN]and y<windsize[1]-l:
        y+=speed
    if keys[pygame.K_RIGHT]and x<windsize[0]-w:
        x+=speed
    if keys[pygame.K_1]:
        r=False
    
    display.fill(black)
    pygame.draw.rect(display,blue,(x,y,w,l))
    pygame.display.update()

pygame.quit()
quit()

