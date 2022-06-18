
import pygame
import os
  
pygame.init()

ASSETS_PATH = './'
FPS = 60
clock = pygame.time.Clock()
#dung de ve inputbox
COLOR_INACTIVE = pygame.Color('grey')
COLOR_ACTIVE = pygame.Color('pink')
FONT = pygame.font.Font(None, 32)
game_guide = pygame.image.load('Group_6.png')
color = pygame.Color('pink')
text_color = pygame.Color('black')
  
# Create Screen
x_screen = 900
y_screen = 600
screen = pygame.display.set_mode((x_screen, y_screen))
screen.fill((255,255,255))
x_mid = x_screen // 2
y_mid = y_screen // 2

# Title of screen
pygame.display.set_caption("Wero - Wordle")

# Text title
title_size = 50

font_title = pygame.font.SysFont("Times New Roman", title_size, bold=True)
font_end_game = pygame.font.SysFont("comicsans", 100)

x_namegame = (x_screen // 2)
y_namegame = 0

wordle = font_title.render('Worlde', True, (0, 0, 0))
vietnam = font_title.render('VietNam', True, (255, 51, 153))
game_win = font_end_game.render('You win', True, (0, 255, 0))
game_lose = font_end_game.render('You lose', True, (0, 50, 100))

#color, x, y, width, height, text, text_size, text_color, font_name
class button():
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
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True    
        return False

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
def isOver(x, y, width, height):
    #Pos is the mouse position or a tuple of (x,y) coordinates
    pos = pygame.mouse.get_pos()
    if pos[0] > x and pos[0] < x + width:
        if pos[1] > y and pos[1] < y + height:
            return True    
    return False
def isClick(x, y, width, height):
    #print(x, y, width, height)
    if isOver(x, y, width, height): return True
    return False
image_position = [[30, 70], [30, 400], [274, 400]]
image_size = [[444, 300], [200, 180], [200, 180]]
#hint_list = ["Da_Nang", "Danh_lam_Quang_Nam", "Danh_lam_Quang_Binh"]
# hint_list = ['4.1.png', '4.2.png', '4.3.png']
#hint_list = ['4.1', '4.2', '4.3']
import random
hint_list = []
def random_question():    
    a = random.randint(1,5)
    for i in range(1,4):
        filename = str(a) + '.' + str(i)        
        hint_list.append(filename)
    print(hint_list)
    return hint_list
   
random_question()


def replaceClickedImage(position, size, hint_list):
    for i in range(1, 3):
        if isClick(position[i][0], position[i][1], size[i][0], size[i][1]) == True:
            a = hint_list[0]
            hint_list[0] = hint_list[i]
            hint_list[i] = a
    return hint_list
#image_list, x, y, width, height
def draw(image_list, x, y, width, height):
    images = province_map(image_list, x, y, width, height)
    images.load_image()
    images.draw_image()
def show_hint(hints):
    for i in range(len(hints)):
        draw([hints[i] + ".png"], image_position[i][0], image_position[i][1], image_size[i][0], image_size[i][1])
        
        
        
        
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        #self.enter = pygame.Rect(x, y, w, h)
        
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
                    check_input(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
        return True
    def draw(self, screen):
        # Blit th screen
        #screen.blit(bg,(0,0))
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+18))
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
             font = pygame.font.SysFont('comicsan',50)
             text = font.render(self.text,1,(0,0,0))
             screen.blit(text,(self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
                     
def check_input(user_text):
    result = []
    cities = ['an giang','ba ria-vung tau','bac giang','bac kan','bac lieu','bac ninh','ben tre','binh dinh','binh duong','binh phuoc','binh thuan','ca mau','can tho','cao bang','da nang','dak lak','dak nong','dien bien','dong nai', 'dong thap','gia lai','ha giang','ha nam','ha noi','hai duong','ha tinh','hai duong','hai phong','hau giang','hoa binh','ho chi minh','hung yen','khanh hoa','kien giang','kon tum','lai chau','lam dong','lang son','lao cai','long an','nam dinh','nghe an','ninh binh','ninh thuan','phu tho','phu yen','quang binh','quang nam','quang ngai','quang ninh','quang tri','soc trang','son la','tay ninh','thai binh','thai nguyen','thanh hoa','thua thien hue','tien giang','tra vinh','tuyen quang','vinh long','vinh phuc','yen bai']
    
    answer = user_text 
    answer = answer.lower()
    check_answer = 0 
    if answer in cities:        
        check_answer = 1
    if  check_answer == 1:
        print(answer)     
    else:
        print('khong tim thay')
        
    return answer


button_1 = Button(397,500,465,55,'Enter')
button_2 = Button(30,10,35,35,'?')
buttons = [button_1,button_2]
input_box1 = InputBox(397,434,465,55)
input_boxes = [input_box1]

done = False
ok = 0        
        
        
# running game

exit = False
result = None
while not exit:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():

        game_guide = pygame.image.load('Group_6.png')
        if event.type == pygame.QUIT:
            done = True
        for box in input_boxes:
            box.handle_event(event)
                
                
        for bt in buttons:
            if bt.isOver(event):
                if bt == buttons[0]:                    
                    check_input(input_box1.text)
                    input_box1.text = ''
                    input_box1.txt_surface = FONT.render(input_box1.text, True, input_box1.color)
                        

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
    screen.fill((255,255,255))
    for bt in buttons:
        bt.draw(screen)
    for box in input_boxes:
        box.draw(screen)
         
    screen.blit(wordle, wordle.get_rect(center = (x_namegame - 90, 20)))
    screen.blit(vietnam, vietnam.get_rect(center = (x_namegame + 90, 20)))
    show_hint(hint_list)
    
    if ok == 1:
        screen.blit(game_guide,(90,90))
    pygame.display.update()
    if result == "win":
        winning_rect = button((0,150,0), x_mid - 250, y_mid - 100, 500, 200, 'You win', 100, (255, 255, 0))
        winning_rect.draw(screen)
    elif result == "lose":
        winning_rect = button((255,255,0), x_mid - 250, y_mid - 100, 500, 200, 'You lose', 100, (255, 0, 0))
        winning_rect.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()