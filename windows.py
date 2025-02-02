import pygame
pygame.init()
story=pygame.display.set_mode((500,500))
flg=False
while not flg:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(story,(30,100,200),pygame.Rect(3,4,45,50))
    pygame.draw.circle(story,(255,0,0),(200,300),100)
    pygame.draw.circle(story,(255,0,0),(110,120),100,10)
    pygame.display.flip()