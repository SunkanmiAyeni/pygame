import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize display surface and set title

display_surface = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Adding image and background image')

# Load and scale images directly

background_image = pygame.transform.scale(

pygame.image.load('background.png').convert(),

(500, 500))

penguin_image = pygame.transform.scale(

pygame.image.load('hello penguin.png').convert_alpha(), (200, 200))

penguin_rect = penguin_image.get_rect(center=(250,

220))

# Initialize font, render text, and set text position

text = pygame.font.Font(None, 36).render('Hello World ', True,

pygame.Color('black'))

text_rect = text.get_rect(center=(250, 360))

def game_loop():
    clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

display_surface.blit(background_image, (0, 0))

display_surface.blit(penguin_image, penguin_rect)

display_surface.blit(text, text_rect)

pygame.display.flip 


pygame.quit()

if __name__ == '__main__':
    game_loop()