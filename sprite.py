import pygame
pygame.init()
story=pygame.display.set_mode((500,500))
flg=False
colours={
    "red":pygame.Color("red"),
    "black":pygame.Color("black"),
    "orange":pygame.Color("orange"),
    "yellow":pygame.Color("yellow"),
    "pink":pygame.Color("pink")
}
currentcolour=colours["yellow"]
x,y=30,30
w,h=60,60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    press=pygame.key.get_pressed()
    if press[pygame.K_LEFT]: x-=3
    if press[pygame.K_DOWN]: y+=3
    if press[pygame.K_RIGHT]: x+=3
    if press[pygame.K_UP]: y-=3
    x=min(max(0,x),500-60)
    y=min(max(0,y),500-60)
    if x==0:currentcolour=colours["black"]
    elif x==440:currentcolour=colours["pink"]
    elif y==0:currentcolour=colours["orange"]
    elif y==440:currentcolour=colours["red"]
    else:
        currentcolour=colours["yellow"]
    story.fill((255,255,255))
    pygame.draw.rect(story,currentcolour,(x,y,w,h))
    pygame.display.flip()
    clock.tick(30)