import pygame
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import math
import os
import random

geolocator = Nominatim(user_agent="MyApp")
pygame.init()

# Create Screen
x_screen = 1000
y_screen = 600
screen = pygame.display.set_mode((x_screen, y_screen))

location_color = (255, 51, 153)
background_color = (255, 255, 255)

COLOR_INACTIVE = pygame.Color('grey')
COLOR_ACTIVE = pygame.Color('pink')
FONT = pygame.font.Font(None, 32)
color = pygame.Color('pink')
text_color = pygame.Color('black')

true_color = (0, 204, 0)
false_color = (255, 0, 0)

hint_list = []

# Title of screen
pygame.display.set_caption("Wero - Wordle")

# Text title
title_size = 50
body_size = 30
end_game_size = 100
font_title = pygame.font.SysFont("Times New Roman", title_size, bold=True)
font_body = pygame.font.SysFont("Times New Roman", body_size, bold=True)
font_end_game = pygame.font.SysFont("comicsans", end_game_size, bold=True)

x_namegame = (x_screen // 2)
y_namegame = 0
x_mid = x_screen // 2
y_mid = y_screen // 2


wordle = font_title.render('Wordle', True, (0, 0, 0))
vietnam = font_title.render('VietNam', True, (255, 51, 153))
game_win = font_end_game.render('You win', True, (0, 255, 0))
game_lose = font_end_game.render('You lose', True, (0, 50, 100))



# running game

# arrow direction
arrow_up = pygame.image.load(r'direction\arrow_up.png')
arrow_up = pygame.transform.scale(arrow_up, (80,80))

arrow_down = pygame.image.load(r'direction\arrow_down.png')
arrow_down = pygame.transform.scale(arrow_down, (80,80))

arrow_left = pygame.image.load(r'direction\arrow_left.png')
arrow_left = pygame.transform.scale(arrow_left, (80,80))

arrow_right = pygame.image.load(r'direction\arrow_right.png')
arrow_right = pygame.transform.scale(arrow_right, (80,80))

cities = ['an giang', 'ba ria-vung tau', 'bac giang', 'bac kan', 'bac lieu', 'bac ninh', 'ben tre',
          'binh dinh', 'binh duong', 'binh phuoc', 'binh thuan', 'ca mau', 'can tho', 'cao bang',
          'da nang', 'dak lak', 'dak nong', 'dien bien', 'dong nai', 'dong thap', 'gia lai',
          'ha giang', 'ha nam', 'ha noi', 'hai duong', 'ha tinh', 'hai duong', 'hai phong',
          'hau giang', 'hoa binh', 'ho chi minh', 'hung yen', 'khanh hoa', 'kien giang', 'kon tum',
          'lai chau', 'lam dong', 'lang son', 'lao cai', 'long an', 'nam dinh', 'nghe an',
          'ninh binh', 'ninh thuan', 'phu tho', 'phu yen', 'quang binh', 'quang nam', 'quang ngai',
          'quang ninh', 'quang tri', 'soc trang', 'son la', 'tay ninh', 'thai binh', 'thai nguyen',
          'thanh hoa', 'thua thien hue', 'tien giang', 'tra vinh', 'tuyen quang', 'vinh long',
          'vinh phuc', 'yen bai', 'kien giang']

game_location_index = random.randint(1,len(cities))
game_location = cities[game_location_index]

print(game_location)
# guess_location = 'Lang Son'

fps = 60
timer = pygame.time.Clock()



def draw_checking_box():
    for i in range(0, 5):
        pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 20, y_screen // 16 + 30 + i*70, 170, 50), 2, 5)
        pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 230, y_screen // 16 + 30 + i*70, 170, 50), 2, 5)

# calculate distances of 5 places
def checking_distance(game_location, guess_location, distance=0):
    # calculate distance
    guess = guess_location
    location_1 = geolocator.geocode(guess)
    location_2 = geolocator.geocode(game_location)
    loc1 = (location_1.latitude, location_1.longitude)
    loc2 = (location_2.latitude, location_2.longitude)
    dis = str(int(geodesic(loc1, loc2).km))

    # calculate compass direction
    alpha_1 = loc1[1] * (math.pi / 180)
    alpha_2 = loc2[1] * math.pi / 180
    phi_1 = loc1[0] * math.pi / 180
    phi_2 = loc2[0] * math.pi / 180
    delta_alpha = (alpha_2 - alpha_1)
    y = math.sin(delta_alpha) * math.cos(phi_2)
    x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
    angle = math.atan2(y, x)
    bearing = int((angle * 180 / math.pi + 360) % 360)
    return dis, bearing

def draw_distance_direction(dis, bearing, number, guess_location):
    guess = guess_location
    guess1 = font_body.render(guess, True, location_color)
    distance = font_body.render(dis, True, location_color)
    screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 105, y_screen // 16 + 54 + 70*number)))
    screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 315, y_screen // 16 + 54 + 70*number)))
    if dis == '0':
        pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 + 20, y_screen // 16 + 30 + number*70, 170, 50), 2, 5)
    else:
        pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 + 20, y_screen // 16 + 30 + number*70, 170, 50), 2, 5)
    
    if '0' == dis:
        pygame.draw.circle(screen, location_color, (x_screen // 2 + 465, y_screen // 16 + 55 + number*70), 25, 5)
        pygame.draw.circle(screen, location_color, (x_screen // 2 + 465, y_screen // 16 + 55 + number*70), 5, 5)
    elif 0 <= bearing < 90:
        #pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70),
                         #(x_screen // 2 + 405, y_screen // 16 + 15 + number*70), 5)

        screen.blit(arrow_up, (x_screen // 2 + 360, y_screen // 16 + 15 + number*70))
    elif 90 <= bearing < 180:
        #pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70),
        #                 (x_screen // 2 + 425, y_screen // 16 + 35 + number*70), 5)
        screen.blit(arrow_right, (x_screen // 2 + 420, y_screen // 16 + 15 + number * 70))
    elif 180 <= bearing < 270:
        #pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70),
        #                 (x_screen // 2 + 405, y_screen // 16 + 55 + number*70), 5)
        screen.blit(arrow_down, (x_screen // 2 + 420, y_screen // 16 + 15 + number * 70))
    elif 270 <= bearing < 360:
        #pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70),
        #                 (x_screen // 2 + 385, y_screen // 16 + 35 + number*70), 5)
        screen.blit(arrow_left, (x_screen // 2 + 420, y_screen // 16 + 15 + number * 70))
    print(dis)
    print(bearing)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        # self.enter = pygame.Rect(x, y, w, h)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = self.text.lower()
                    cities = ['an giang', 'ba ria-vung tau', 'bac giang', 'bac kan', 'bac lieu', 'bac ninh', 'ben tre',
                              'binh dinh', 'binh duong', 'binh phuoc', 'binh thuan', 'ca mau', 'can tho', 'cao bang',
                              'da nang', 'dak lak', 'dak nong', 'dien bien', 'dong nai', 'dong thap', 'gia lai',
                              'ha giang', 'ha nam', 'ha noi', 'hai duong', 'ha tinh', 'hai duong', 'hai phong',
                              'hau giang', 'hoa binh', 'ho chi minh', 'hung yen', 'khanh hoa', 'kien giang', 'kon tum',
                              'lai chau', 'lam dong', 'lang son', 'lao cai', 'long an', 'nam dinh', 'nghe an',
                              'ninh binh', 'ninh thuan', 'phu tho', 'phu yen', 'quang binh', 'quang nam', 'quang ngai',
                              'quang ninh', 'quang tri', 'soc trang', 'son la', 'tay ninh', 'thai binh', 'thai nguyen',
                              'thanh hoa', 'thua thien hue', 'tien giang', 'tra vinh', 'tuyen quang', 'vinh long',
                              'vinh phuc', 'yen bai']
                    if self.text in cities:
                        return self.text
                    else:
                        return False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
        return False
    def draw(self, screen):
        # Blit th screen
        # screen.blit(bg,(0,0))
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 18))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
#
class show_instruction():
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.enter = pygame.Rect(x, y, w, h)
    def draw(self, screen):
         pygame.draw.rect(screen, self.color, self.rect, 0)
         if self.text != '':
             font = pygame.font.SysFont('comicsan',50)
             text = font.render(self.text,1,(0,0,0))
             screen.blit(text,(self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))

class province_map():
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
        pygame.draw.rect(screen, (255, 255, 255), (self.x - 1, self.y - 1, self.width + 2, self.height + 2), width=0)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 1, self.y - 1, self.width + 2, self.height + 2), 2, border_radius = 4)
        screen.blit(self.image, (self.x, self.y))

class Enter_button():
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        if self.text != '':
            font = pygame.font.SysFont('comicsan', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True

class win_lose_button():
    def __init__(self, color, x, y, width, height, text='', text_size=40, text_color=(0,0,0), font_name='comicsans'):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.font_name = font_name
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        if self.text != '':
            font = pygame.font.SysFont(self.font_name, self.text_size)
            text = font.render(self.text, True, self.text_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        return False

image_position = [[30, 70], [30, 400], [274, 400]]
image_size = [[444, 300], [200, 180], [200, 180]]
hint_list = []



# giving hint function
#
def get_hint(city_index):
    a = (city_index % 5) + 1
    print('a: ' + str(a))
    for i in range(1, 4):
        filename = str(a) + '.' + str(i)
        hint_list.append(filename)
    print(hint_list)
    return hint_list
get_hint(game_location_index)

def replaceClickedImage(position, size, hint_list):
    for i in range(0, 3):
        if isClick(position[i][0], position[i][1], size[i][0], size[i][1]) == True:
            if i == 0:
                a = hint_list[1]
                b = hint_list[2]
                hint_list[2] = hint_list[0]
                hint_list[0] = a
                hint_list[1] = b
            else:
                a = hint_list[0]
                hint_list[0] = hint_list[i]
                hint_list[i] = a
    return hint_list
def draw(image_list, x, y, width, height, outline = False):
    image = images(image_list, x, y, width, height, outline)
    image.load_image()
    image.draw_image()
def show_hint(hints):
    for i in range(len(hints)):
        draw([hints[i] + ".png"], image_position[i][0], image_position[i][1], image_size[i][0], image_size[i][1], outline = True)
def isOver(x, y, width, height):
        #Pos is the mouse position or a tuple of (x,y) coordinates
    pos = pygame.mouse.get_pos()
    if pos[0] > x and pos[0] < x + width:
        if pos[1] > y and pos[1] < y + height:
            return True
    return False
def isClick(x, y, width, height):
        # print(x, y, width, height)
    if isOver(x, y, width, height): return True
    return False


x = 0
exit = False
guess_list = []
dis_list = []
bearing_list = []

ASSETS_PATH = './'
game_guide = pygame.image.load('Group_6.png')
ok = 0

image_position = [[30, 70], [30, 400], [274, 400]]
image_size = [[444, 300], [200, 180], [200, 180]]

enter_button = Enter_button(x_screen // 2 + 20, 500, 380, 55, 'Enter')
instruction_button = show_instruction(30,10,35,35,'?')
enter_button_list = [enter_button]
instruction_button_list = [instruction_button]


input_box1 = InputBox(x_screen // 2 + 20, 434, 380, 55)
input_boxes = [input_box1]

# Thay duong dan logo vao day
#             |
#             |
#             V
draw(["logo/Nen trang.png"], -50, -200, 1000, 1000)
pygame.display.update()
time.sleep(4)

while not exit:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    timer.tick(fps)
    screen.fill(background_color)
    screen.blit(wordle, wordle.get_rect(center=(x_namegame - 95, 20)))
    screen.blit(vietnam, vietnam.get_rect(center=(x_namegame + 95, 20)))
    draw_checking_box()
    #print(hint_list)
    show_hint(hint_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        for box in input_boxes:
            box.handle_event(event)
        for bt in enter_button_list:
            if bt.isOver(event):
                print(input_box1.text)
                if input_box1.text in cities:
                    guess_list.append(input_box1.text)
                    dis, bearing = checking_distance(game_location=game_location, guess_location=guess_list[-1])
                    dis_list.append(dis)
                    bearing_list.append(bearing)
                    x += 1
                    input_box1.text = ''
                    input_box1.txt_surface = FONT.render(input_box1.text, True, input_box1.color)
                else:
                    print('Nothing')
        if event.type == pygame.MOUSEBUTTONDOWN:
            hint_list = replaceClickedImage(image_position, image_size, hint_list)
            if event.button == 1:
                    if (30 < mouse_x < 65) and (10 < mouse_y < 50):
                        ok = 1
                    else:
                        ok = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit = True
        if event.type == pygame.QUIT:
            exit = True

    for bt in enter_button_list:
        bt.draw(screen)
    for bt in instruction_button_list:
        bt.draw(screen)
    for box in input_boxes:
        box.draw(screen)
    # if result == "win":
    #     winning_rect = button((0, 150, 0), x_mid - 250, y_mid - 100, 500, 200, 'You win', 100, (255, 255, 0))
    #     winning_rect.draw(screen)
    # elif result == "lose":
    #     winning_rect = button((255, 255, 0), x_mid - 250, y_mid - 100, 500, 200, 'You lose', 100, (255, 0, 0))
    #     winning_rect.draw(screen)

    if x == 1:
        draw_distance_direction(dis=dis_list[x - 1], bearing=bearing_list[x - 1], guess_location=guess_list[x - 1],
                                number=x - 1)
    if x == 2:
        draw_distance_direction(dis=dis_list[x - 2], bearing=bearing_list[x - 2], guess_location=guess_list[x - 2],
                                number=x - 2)
        draw_distance_direction(dis=dis_list[x - 1], bearing=bearing_list[x - 1], guess_location=guess_list[x - 1],
                                number=x - 1)
    if x == 3:
        draw_distance_direction(dis=dis_list[x - 3], bearing=bearing_list[x - 3], guess_location=guess_list[x - 3],
                                number=x - 3)
        draw_distance_direction(dis=dis_list[x - 2], bearing=bearing_list[x - 2], guess_location=guess_list[x - 2],
                                number=x - 2)
        draw_distance_direction(dis=dis_list[x - 1], bearing=bearing_list[x - 1], guess_location=guess_list[x - 1],
                                number=x - 1)
    if x == 4:
        draw_distance_direction(dis=dis_list[x - 4], bearing=bearing_list[x - 4], guess_location=guess_list[x - 4],
                                number=x - 4)
        draw_distance_direction(dis=dis_list[x - 3], bearing=bearing_list[x - 3], guess_location=guess_list[x - 3],
                                number=x - 3)
        draw_distance_direction(dis=dis_list[x - 2], bearing=bearing_list[x - 2], guess_location=guess_list[x - 2],
                                number=x - 2)
        draw_distance_direction(dis=dis_list[x - 1], bearing=bearing_list[x - 1], guess_location=guess_list[x - 1],
                                number=x - 1)
    if x == 5:
        draw_distance_direction(dis=dis_list[x - 5], bearing=bearing_list[x - 5], guess_location=guess_list[x - 5],
                                number=x - 5)
        draw_distance_direction(dis=dis_list[x - 4], bearing=bearing_list[x - 4], guess_location=guess_list[x - 4],
                                number=x - 4)
        draw_distance_direction(dis=dis_list[x - 3], bearing=bearing_list[x - 3], guess_location=guess_list[x - 3],
                                number=x - 3)
        draw_distance_direction(dis=dis_list[x - 2], bearing=bearing_list[x - 2], guess_location=guess_list[x - 2],
                                number=x - 2)
        draw_distance_direction(dis=dis_list[x - 1], bearing=bearing_list[x - 1], guess_location=guess_list[x - 1],
                                number=x - 1)
    if ok == 1:
        screen.blit(game_guide, (90, 90))

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
