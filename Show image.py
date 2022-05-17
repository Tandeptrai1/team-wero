import pygame
import os
  
pygame.init()

ASSETS_PATH = './'
FPS = 60
clock = pygame.time.Clock()
  
# Create Screen
x_screen = 1000
y_screen = 800
screen = pygame.display.set_mode((x_screen, y_screen))
screen.fill((255,255,255))

# Title of screen
pygame.display.set_caption("Wero - Wordle")

# Show image funtion
class image():
    def __init__(self, image_list, x, y, width, height):
        self.image_list = image_list
        self.image = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def load_image(self):
        for image in self.image_list:
            self.surface = pygame.image.load(os.path.join(ASSETS_PATH, image))
    def draw_image(self):
        self.image = self.surface
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.x, self.y))
def draw_image(image_list, x, y, width, height):
    images = image(image_list, x, y, width, height)
    images.load_image()
    images.draw_image()

# running game
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    draw_image(["example.png"], 100, 100, 500, 500)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()