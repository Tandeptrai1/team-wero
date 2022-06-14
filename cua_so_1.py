import pygame
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import math

geolocator = Nominatim(user_agent="MyApp")
pygame.init()

# Create Screen
x_screen = 1000
y_screen = 800
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
# Title of screen
pygame.display.set_caption("Wero - Wordle")

# Text title
text_size_1 = 50
text_size_2 = 30
font_1 = pygame.font.SysFont("Times New Roman", text_size_1, bold=True)
font_2 = pygame.font.SysFont("Times New Roman", text_size_2, bold=True)
x_namegame = (x_screen // 2)
y_namegame = 0

wordle = font_1.render('Wordle', True, (0, 0, 0))
vietnam = font_1.render('VietNam', True, (255, 51, 153))
# running game

game_location = 'Can Tho'
# guess_location = 'Lang Son'

fps = 60
timer = pygame.time.Clock()

def draw_checking_box():
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 10, 170, 50), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 170, y_screen // 16 + 10, 170, 50), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35), 25, 5)
    # pygame.draw.line(screen, location_color, (x_screen// 2 + 405, y_screen//16 + 100), (x_screen// 2 + 420, y_screen//16 + 100), 4)

    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 80, 170, 50), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 170, y_screen // 16 + 80, 170, 50), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 105), 25, 5)

    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 150, 170, 50), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 170, y_screen // 16 + 150, 170, 50), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 175), 25, 5)

    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 220, 170, 50), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 170, y_screen // 16 + 220, 170, 50), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 245), 25, 5)

    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 290, 170, 50), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 170, y_screen // 16 + 290, 170, 50), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 315), 25, 5)

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
    guess1 = font_2.render(guess, True, location_color)
    distance = font_2.render(dis, True, location_color)
    screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 45, y_screen // 16 + 34 + 70*number)))
    screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 255, y_screen // 16 + 34 + 70*number)))
    if dis == '0':
        pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 10 + number*70, 170, 50), 2, 5)
    else:
        pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 10 + number*70, 170, 50), 2, 5)
    
    if '0' == dis:
        pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70), 5, 5)
    elif 0 <= bearing < 90:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70),
                         (x_screen // 2 + 405, y_screen // 16 + 15 + number*70), 5)
    elif 90 <= bearing < 180:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70),
                         (x_screen // 2 + 425, y_screen // 16 + 35 + number*70), 5)
    elif 180 <= bearing < 270:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70),
                         (x_screen // 2 + 405, y_screen // 16 + 55 + number*70), 5)
    elif 270 <= bearing < 360:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 35 + number*70),
                         (x_screen // 2 + 385, y_screen // 16 + 35 + number*70), 5)
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


class Button():
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

# def checking_distance_2(game_location, guess_location, distance=0):
#     guess = guess_location
#     location_1 = geolocator.geocode(guess)
#     location_2 = geolocator.geocode(game_location)
#     loc1 = (location_1.latitude, location_1.longitude)
#     loc2 = (location_2.latitude, location_2.longitude)
#     dis = str(int(geodesic(loc1, loc2).km))
#     guess1 = font_2.render(guess, True, (255, 51, 153))
#     distance = font_2.render(dis, True, (255, 51, 153))
#     screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 45, y_screen // 16 + 104)))
#     screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 255, y_screen // 16 + 104)))
#     if dis == '0':
#         pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 80, 170, 50), 2, 5)
#     else:
#         pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 80, 170, 50), 2, 5)
#
#     alpha_1 = loc1[1] * (math.pi / 180)
#     alpha_2 = loc2[1] * math.pi / 180
#     phi_1 = loc1[0] * math.pi / 180
#     phi_2 = loc2[0] * math.pi / 180
#     delta_alpha = (alpha_2 - alpha_1)
#     y = math.sin(delta_alpha) * math.cos(phi_2)
#     x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
#     angle = math.atan2(y, x)
#     bearing = int((angle * 180 / math.pi + 360) % 360)
#     if '0' == dis:
#         pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 105), 5, 5)
#     elif 0 <= bearing < 90:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 105),
#                          (x_screen // 2 + 405, y_screen // 16 + 85), 5)
#     elif 90 <= bearing < 180:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 105),
#                          (x_screen // 2 + 425, y_screen // 16 + 105), 5)
#     elif 180 <= bearing < 270:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 105),
#                          (x_screen // 2 + 405, y_screen // 16 + 125), 5)
#     elif 270 <= bearing < 360:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 105),
#                          (x_screen // 2 + 385, y_screen // 16 + 105), 5)
#     print(dis)
#
#
# def checking_distance_3(game_location, guess_location, distance=0):
#     guess = guess_location
#     location_1 = geolocator.geocode(guess)
#     location_2 = geolocator.geocode(game_location)
#     loc1 = (location_1.latitude, location_1.longitude)
#     loc2 = (location_2.latitude, location_2.longitude)
#     dis = str(int(geodesic(loc1, loc2).km))
#     guess1 = font_2.render(guess, True, (255, 51, 153))
#     distance = font_2.render(dis, True, (255, 51, 153))
#     screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 45, y_screen // 16 + 174)))
#     screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 255, y_screen // 16 + 174)))
#     if dis == '0':
#         pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 150, 170, 50), 2, 5)
#     else:
#         pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 150, 170, 50), 2, 5)
#
#     alpha_1 = loc1[1] * (math.pi / 180)
#     alpha_2 = loc2[1] * math.pi / 180
#     phi_1 = loc1[0] * math.pi / 180
#     phi_2 = loc2[0] * math.pi / 180
#     delta_alpha = (alpha_2 - alpha_1)
#     y = math.sin(delta_alpha) * math.cos(phi_2)
#     x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
#     angle = math.atan2(y, x)
#     bearing = int((angle * 180 / math.pi + 360) % 360)
#     if '0' == dis:
#         pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 175), 5, 5)
#     elif 0 <= bearing < 90:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 175),
#                          (x_screen // 2 + 405, y_screen // 16 + 155), 5)
#     elif 90 <= bearing < 180:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 170),
#                          (x_screen // 2 + 425, y_screen // 16 + 170), 5)
#     elif 180 <= bearing < 270:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 175),
#                          (x_screen // 2 + 405, y_screen // 16 + 195), 5)
#     elif 270 <= bearing < 360:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 190),
#                          (x_screen // 2 + 390, y_screen // 16 + 170), 5)
#     print(dis)
#
#
# def checking_distance_4(game_location, guess_location, distance=0):
#     guess = guess_location
#     location_1 = geolocator.geocode(guess)
#     location_2 = geolocator.geocode(game_location)
#     loc1 = (location_1.latitude, location_1.longitude)
#     loc2 = (location_2.latitude, location_2.longitude)
#     dis = str(int(geodesic(loc1, loc2).km))
#     guess1 = font_2.render(guess, True, (255, 51, 153))
#     distance = font_2.render(dis, True, (255, 51, 153))
#     screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 45, y_screen // 16 + 244)))
#     screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 255, y_screen // 16 + 244)))
#
#     if dis == '0':
#         pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 220, 170, 50), 2, 5)
#     else:
#         pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 220, 170, 50), 2, 5)
#
#     alpha_1 = loc1[1] * (math.pi / 180)
#     alpha_2 = loc2[1] * math.pi / 180
#     phi_1 = loc1[0] * math.pi / 180
#     phi_2 = loc2[0] * math.pi / 180
#     delta_alpha = (alpha_2 - alpha_1)
#     y = math.sin(delta_alpha) * math.cos(phi_2)
#     x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
#     angle = math.atan2(y, x)
#     bearing = int((angle * 180 / math.pi + 360) % 360)
#     if '0' == dis:
#         pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 245), 5, 5)
#     elif 0 <= bearing < 90:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 245),
#                          (x_screen // 2 + 405, y_screen // 16 + 225), 5)
#     elif 90 <= bearing < 180:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 240),
#                          (x_screen // 2 + 425, y_screen // 16 + 240), 5)
#     elif 180 <= bearing < 270:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 245),
#                          (x_screen // 2 + 405, y_screen // 16 + 265), 5)
#     elif 270 <= bearing < 360:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 255),
#                          (x_screen // 2 + 390, y_screen // 16 + 235), 5)
#     print(dis)
#
#
# def checking_distance_5(game_location, guess_location, distance=0):
#     guess = guess_location
#     location_1 = geolocator.geocode(guess)
#     location_2 = geolocator.geocode(game_location)
#     loc1 = (location_1.latitude, location_1.longitude)
#     loc2 = (location_2.latitude, location_2.longitude)
#     dis = str(int(geodesic(loc1, loc2).km))
#     guess1 = font_2.render(guess, True, (255, 51, 153))
#     distance = font_2.render(dis, True, (255, 51, 153))
#     screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 45, y_screen // 16 + 314)))
#     screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 255, y_screen // 16 + 314)))
#     if dis == '0':
#         pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 290, 170, 50), 2, 5)
#     else:
#         pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 - 40, y_screen // 16 + 290, 170, 50), 2, 5)
#
#     alpha_1 = loc1[1] * (math.pi / 180)
#     alpha_2 = loc2[1] * math.pi / 180
#     phi_1 = loc1[0] * math.pi / 180
#     phi_2 = loc2[0] * math.pi / 180
#     delta_alpha = (alpha_2 - alpha_1)
#     y = math.sin(delta_alpha) * math.cos(phi_2)
#     x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
#     angle = math.atan2(y, x)
#     bearing = int((angle * 180 / math.pi + 360) % 360)
#     if '0' == dis:
#         pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 315), 5, 5)
#     elif 0 <= bearing < 90:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 310),
#                          (x_screen // 2 + 405, y_screen // 16 + 290), 5)
#     elif 90 <= bearing < 180:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 310),
#                          (x_screen // 2 + 425, y_screen // 16 + 310), 5)
#     elif 180 <= bearing < 270:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 315),
#                          (x_screen // 2 + 405, y_screen // 16 + 335), 5)
#     elif 270 <= bearing < 360:
#         pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 325),
#                          (x_screen // 2 + 390, y_screen // 16 + 305), 5)
#     print(dis)

# def checking_distance(x, game_location, guess_location, distance = 0):
#         guess_1 = ''
#         guess_2 = ''
#         guess_3 = ''
#         guess_4 = ''
#         guess_5 = ''
#         dis_1 = ''
#         dis_2 = ''
#         if x == 1:
#             guess_1 = guess_location
#             location_1 = geolocator.geocode(game_location)
#             location_2 = geolocator.geocode(guess_1)
#             loc1 = (location_1.latitude, location_1.longitude)
#             loc2 = (location_2.latitude, location_2.longitude)
#             dis_1 = str(int(geodesic(loc1, loc2).km))
#         guess1 = font_2.render(guess_1, True, (255, 51, 153))
#         distance_1 = font_2.render(dis_1, True, (255, 51, 153))
#         screen.blit(guess1, guess1.get_rect(center = (x_screen// 2 + 150, y_screen//16 + 30)))
#         screen.blit(distance_1, distance_1.get_rect(center = (x_screen// 2 + 290, y_screen//16 + 30)))
#         print(dis_1)
#         if x == 2:
#             guess_2 = guess_location
#
#             location_1 = geolocator.geocode(game_location)
#             location_2 = geolocator.geocode(guess_2)
#             loc1 = (location_1.latitude, location_1.longitude)
#             loc2 = (location_2.latitude, location_2.longitude)
#             dis_2 = str(int(geodesic(loc1, loc2).km))
#
#             screen.blit(guess1, guess1.get_rect(center = (x_screen// 2 + 150, y_screen//16 + 30)))
#             screen.blit(distance_1, distance_1.get_rect(center = (x_screen// 2 + 290, y_screen//16 + 30)))
#             print(dis_1)
#
#             guess2 = font_2.render(guess_2, True, (255, 51, 153))
#             distance_2 = font_2.render(dis_2, True, (255, 51, 153))
#             screen.blit(guess2, guess2.get_rect(center = (x_screen// 2 + 150, y_screen//16 + 100)))
#             screen.blit(distance_2, distance_2.get_rect(center = (x_screen// 2 + 290, y_screen//16 + 100)))
#             print(dis_2)





x = 0
exit = False
guess_list = []
dis_list = []
bearing_list = []


button_1 = Button(397, 500, 465, 55, 'Enter')
buttons = [button_1]
input_box1 = InputBox(397, 434, 465, 55)
input_boxes = [input_box1]

while not exit:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    timer.tick(fps)
    for event in pygame.event.get():
        screen.fill(background_color)
        screen.blit(wordle, wordle.get_rect(center=(x_namegame - 95, 20)))
        screen.blit(vietnam, vietnam.get_rect(center=(x_namegame + 95, 20)))
        draw_checking_box()
        if event.type == pygame.QUIT:
            exit = True
        for box in input_boxes:
            box.handle_event(event)
        for bt in buttons:
            if bt.isOver(event):
                print(input_box1.text)
                guess_list.append(input_box1.text)
                dis, bearing = checking_distance(game_location=game_location, guess_location=guess_list[-1])
                dis_list.append(dis)
                bearing_list.append(bearing)
                x += 1

    for bt in buttons:
        bt.draw(screen)
    for box in input_boxes:
        box.draw(screen)
    print(guess_list)
    print(dis_list)
    print(bearing_list)
    print(x)

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


    pygame.display.update()
    pygame.display.flip()
    # checking_distance(x, game_location, guess_location)
    # if x == 1:
    #    guess_location = str(input())
    #    checking_distance(x, game_location, guess_location)
pygame.quit()