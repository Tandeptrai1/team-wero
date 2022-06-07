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
true_color = (0, 204, 0)
false_color = (255, 0, 0)
# Title of screen
pygame.display.set_caption("Wero - Wordle")

# Text title
text_size_1 = 30
text_size_2 = 15
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


def draw_checking_distance():
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 10, 100, 40), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 240, y_screen // 16 + 10, 100, 40), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 30), 20, 5)
    # pygame.draw.line(screen, location_color, (x_screen// 2 + 405, y_screen//16 + 100), (x_screen// 2 + 420, y_screen//16 + 100), 4)

    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 80, 100, 40), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 240, y_screen // 16 + 80, 100, 40), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 100), 20, 5)

    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 150, 100, 40), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 240, y_screen // 16 + 150, 100, 40), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 170), 20, 5)

    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 220, 100, 40), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 240, y_screen // 16 + 220, 100, 40), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 240), 20, 5)

    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 290, 100, 40), 2, 5)
    pygame.draw.rect(screen, location_color, pygame.Rect(x_screen // 2 + 240, y_screen // 16 + 290, 100, 40), 2, 5)
    pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 310), 20, 5)


# calculate distances of 5 places
def checking_distance_1(game_location, guess_location, distance=0):
    # calculate distance
    guess = guess_location
    location_1 = geolocator.geocode(game_location)
    location_2 = geolocator.geocode(guess)
    loc1 = (location_1.latitude, location_1.longitude)
    loc2 = (location_2.latitude, location_2.longitude)
    dis = str(int(geodesic(loc1, loc2).km))
    guess1 = font_2.render(guess, True, (255, 51, 153))
    distance = font_2.render(dis, True, (255, 51, 153))
    screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 150, y_screen // 16 + 30)))
    screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 290, y_screen // 16 + 30)))
    if dis == '0':
        pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 10, 100, 40), 2, 5)
    else:
        pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 10, 100, 40), 2, 5)
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
    if '0' == dis:
        pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 30), 5, 5)
    elif 0 <= bearing < 90:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 30),
                         (x_screen // 2 + 405, y_screen // 16 + 15), 4)
    elif 90 <= bearing < 180:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 30),
                         (x_screen // 2 + 420, y_screen // 16 + 30), 4)
    elif 180 <= bearing < 270:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 30),
                         (x_screen // 2 + 405, y_screen // 16 + 45), 4)
    elif 270 <= bearing < 360:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 45),
                         (x_screen // 2 + 390, y_screen // 16 + 30), 4)
    print(dis)
    print(bearing)


def checking_distance_2(game_location, guess_location, distance=0):
    guess = guess_location
    location_1 = geolocator.geocode(game_location)
    location_2 = geolocator.geocode(guess)
    loc1 = (location_1.latitude, location_1.longitude)
    loc2 = (location_2.latitude, location_2.longitude)
    dis = str(int(geodesic(loc1, loc2).km))
    guess1 = font_2.render(guess, True, (255, 51, 153))
    distance = font_2.render(dis, True, (255, 51, 153))
    screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 150, y_screen // 16 + 100)))
    screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 290, y_screen // 16 + 100)))
    if dis == '0':
        pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 80, 100, 40), 2, 5)
    else:
        pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 80, 100, 40), 2, 5)

    alpha_1 = loc1[1] * (math.pi / 180)
    alpha_2 = loc2[1] * math.pi / 180
    phi_1 = loc1[0] * math.pi / 180
    phi_2 = loc2[0] * math.pi / 180
    delta_alpha = (alpha_2 - alpha_1)
    y = math.sin(delta_alpha) * math.cos(phi_2)
    x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
    angle = math.atan2(y, x)
    bearing = int((angle * 180 / math.pi + 360) % 360)
    if '0' == dis:
        pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 100), 5, 5)
    elif 0 <= bearing < 90:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 100),
                         (x_screen // 2 + 405, y_screen // 16 + 85), 4)
    elif 90 <= bearing < 180:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 100),
                         (x_screen // 2 + 420, y_screen // 16 + 100), 4)
    elif 180 <= bearing < 270:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 100),
                         (x_screen // 2 + 405, y_screen // 16 + 115), 4)
    elif 270 <= bearing < 360:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 115),
                         (x_screen // 2 + 390, y_screen // 16 + 100), 4)
    print(dis)


def checking_distance_3(game_location, guess_location, distance=0):
    guess = guess_location
    location_1 = geolocator.geocode(game_location)
    location_2 = geolocator.geocode(guess)
    loc1 = (location_1.latitude, location_1.longitude)
    loc2 = (location_2.latitude, location_2.longitude)
    dis = str(int(geodesic(loc1, loc2).km))
    guess1 = font_2.render(guess, True, (255, 51, 153))
    distance = font_2.render(dis, True, (255, 51, 153))
    screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 150, y_screen // 16 + 170)))
    screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 290, y_screen // 16 + 170)))
    if dis == '0':
        pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 150, 100, 40), 2, 5)
    else:
        pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 150, 100, 40), 2, 5)

    alpha_1 = loc1[1] * (math.pi / 180)
    alpha_2 = loc2[1] * math.pi / 180
    phi_1 = loc1[0] * math.pi / 180
    phi_2 = loc2[0] * math.pi / 180
    delta_alpha = (alpha_2 - alpha_1)
    y = math.sin(delta_alpha) * math.cos(phi_2)
    x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
    angle = math.atan2(y, x)
    bearing = int((angle * 180 / math.pi + 360) % 360)
    if '0' == dis:
        pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 170), 5, 5)
    elif 0 <= bearing < 90:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 170),
                         (x_screen // 2 + 405, y_screen // 16 + 155), 4)
    elif 90 <= bearing < 180:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 170),
                         (x_screen // 2 + 420, y_screen // 16 + 170), 4)
    elif 180 <= bearing < 270:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 170),
                         (x_screen // 2 + 405, y_screen // 16 + 185), 4)
    elif 270 <= bearing < 360:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 185),
                         (x_screen // 2 + 390, y_screen // 16 + 170), 4)
    print(dis)


def checking_distance_4(game_location, guess_location, distance=0):
    guess = guess_location
    location_1 = geolocator.geocode(game_location)
    location_2 = geolocator.geocode(guess)
    loc1 = (location_1.latitude, location_1.longitude)
    loc2 = (location_2.latitude, location_2.longitude)
    dis = str(int(geodesic(loc1, loc2).km))
    guess1 = font_2.render(guess, True, (255, 51, 153))
    distance = font_2.render(dis, True, (255, 51, 153))
    screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 150, y_screen // 16 + 240)))
    screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 290, y_screen // 16 + 240)))

    if dis == '0':
        pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 220, 100, 40), 2, 5)
    else:
        pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 220, 100, 40), 2, 5)

    alpha_1 = loc1[1] * (math.pi / 180)
    alpha_2 = loc2[1] * math.pi / 180
    phi_1 = loc1[0] * math.pi / 180
    phi_2 = loc2[0] * math.pi / 180
    delta_alpha = (alpha_2 - alpha_1)
    y = math.sin(delta_alpha) * math.cos(phi_2)
    x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
    angle = math.atan2(y, x)
    bearing = int((angle * 180 / math.pi + 360) % 360)
    if '0' == dis:
        pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 240), 5, 5)
    elif 0 <= bearing < 90:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 240),
                         (x_screen // 2 + 405, y_screen // 16 + 225), 4)
    elif 90 <= bearing < 180:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 240),
                         (x_screen // 2 + 420, y_screen // 16 + 240), 4)
    elif 180 <= bearing < 270:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 240),
                         (x_screen // 2 + 405, y_screen // 16 + 255), 4)
    elif 270 <= bearing < 360:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 255),
                         (x_screen // 2 + 390, y_screen // 16 + 240), 4)
    print(dis)


def checking_distance_5(game_location, guess_location, distance=0):
    guess = guess_location
    location_1 = geolocator.geocode(game_location)
    location_2 = geolocator.geocode(guess)
    loc1 = (location_1.latitude, location_1.longitude)
    loc2 = (location_2.latitude, location_2.longitude)
    dis = str(int(geodesic(loc1, loc2).km))
    guess1 = font_2.render(guess, True, (255, 51, 153))
    distance = font_2.render(dis, True, (255, 51, 153))
    screen.blit(guess1, guess1.get_rect(center=(x_screen // 2 + 150, y_screen // 16 + 310)))
    screen.blit(distance, distance.get_rect(center=(x_screen // 2 + 290, y_screen // 16 + 310)))
    if dis == '0':
        pygame.draw.rect(screen, true_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 290, 100, 40), 2, 5)
    else:
        pygame.draw.rect(screen, false_color, pygame.Rect(x_screen // 2 + 100, y_screen // 16 + 290, 100, 40), 2, 5)

    alpha_1 = loc1[1] * (math.pi / 180)
    alpha_2 = loc2[1] * math.pi / 180
    phi_1 = loc1[0] * math.pi / 180
    phi_2 = loc2[0] * math.pi / 180
    delta_alpha = (alpha_2 - alpha_1)
    y = math.sin(delta_alpha) * math.cos(phi_2)
    x = math.cos(phi_1) * math.sin(phi_2) - math.sin(phi_1) * math.cos(phi_2) * math.cos(delta_alpha)
    angle = math.atan2(y, x)
    bearing = int((angle * 180 / math.pi + 360) % 360)
    if '0' == dis:
        pygame.draw.circle(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 310), 5, 5)
    elif 0 <= bearing < 90:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 310),
                         (x_screen // 2 + 405, y_screen // 16 + 295), 4)
    elif 90 <= bearing < 180:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 310),
                         (x_screen // 2 + 420, y_screen // 16 + 310), 4)
    elif 180 <= bearing < 270:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 310),
                         (x_screen // 2 + 405, y_screen // 16 + 325), 4)
    elif 270 <= bearing < 360:
        pygame.draw.line(screen, location_color, (x_screen // 2 + 405, y_screen // 16 + 325),
                         (x_screen // 2 + 390, y_screen // 16 + 310), 4)
    print(dis)

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


def getting_guess():
    guess = str(input('doan dia diem: '))
    return guess


x = 1
exit = False
guess_1 = ''
guess_2 = ''
guess_3 = ''
guess_4 = ''
guess_5 = ''
guess_6 = ''
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    timer.tick(fps)
    screen.fill(background_color)
    screen.blit(wordle, wordle.get_rect(center=(x_namegame - 55, 20)))
    screen.blit(vietnam, vietnam.get_rect(center=(x_namegame + 55, 20)))
    draw_checking_distance()
    print(x)
    if x == 1:
        guess_1 = getting_guess()
        checking_distance_1(guess_location=guess_1, game_location=game_location)
    if x == 2:
        guess_2 = getting_guess()
        checking_distance_1(guess_location=guess_1, game_location=game_location)
        checking_distance_2(guess_location=guess_2, game_location=game_location)
    if x == 3:
        guess_3 = getting_guess()
        checking_distance_1(guess_location=guess_1, game_location=game_location)
        checking_distance_2(guess_location=guess_2, game_location=game_location)
        checking_distance_3(guess_location=guess_3, game_location=game_location)
    if x == 4:
        guess_4 = getting_guess()
        checking_distance_1(guess_location=guess_1, game_location=game_location)
        checking_distance_2(guess_location=guess_2, game_location=game_location)
        checking_distance_3(guess_location=guess_3, game_location=game_location)
        checking_distance_4(guess_location=guess_4, game_location=game_location)
    if x == 5:
        guess_5 = getting_guess()
        checking_distance_1(guess_location=guess_1, game_location=game_location)
        checking_distance_2(guess_location=guess_2, game_location=game_location)
        checking_distance_3(guess_location=guess_3, game_location=game_location)
        checking_distance_4(guess_location=guess_4, game_location=game_location)
        checking_distance_5(guess_location=guess_5, game_location=game_location)
    if x == 6:
        guess_6 = getting_guess()
    pygame.display.update()
    pygame.display.flip()
    x += 1
    # checking_distance(x, game_location, guess_location)
    # if x == 1:
    #    guess_location = str(input())
    #    checking_distance(x, game_location, guess_location)
pygame.quit()
