import pygame
  
pygame.init()
  
# Create Screen
x_screen = 500
y_screen = 500
screen = pygame.display.set_mode((x_screen, y_screen))
screen.fill((255,255,255))

# Title of screen
pygame.display.set_caption("Wero - Wordle")

# Text title
text_size = 30

font = pygame.font.SysFont("Times New Roman", text_size, bold=True)

x_namegame = (x_screen // 2)
y_namegame = 0

wordle = font.render('Wordle', True, (0, 0, 0))
vietnam = font.render('VietNam', True, (255, 51, 153))
# running game
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    #screen.blit(pygame.font.Font.render(font, "Wordle", 1, color),(x_namegame,y_namegame))
    screen.blit(wordle, wordle.get_rect(center = (x_namegame - 55, 20)))
    screen.blit(vietnam, vietnam.get_rect(center = (x_namegame + 55, 20)))
    pygame.display.update()