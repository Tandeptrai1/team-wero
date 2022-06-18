
import pygame 

pygame.init()
screen = pygame.display.set_mode((900,600))
#bg = pygame.image.load('Group_2.png')
COLOR_INACTIVE = pygame.Color('grey')
COLOR_ACTIVE = pygame.Color('pink')
FONT = pygame.font.Font(None, 32)
game_guide = pygame.image.load('Group_6.png')
color = pygame.Color('pink')
text_color = pygame.Color('black')

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
#                     self.text = self.text.lower()
#                     cities = ['an giang','ba ria-vung tau','bac giang','bac kan','bac lieu','bac ninh','ben tre','binh dinh','binh duong','binh phuoc','binh thuan','ca mau','can tho','cao bang','da nang','dak lak','dak nong','dien bien','dong nai', 'dong thap','gia lai','ha giang','ha nam','ha noi','hai duong','ha tinh','hai duong','hai phong','hau giang','hoa binh','ho chi minh','hung yen','khanh hoa','kien giang','kon tum','lai chau','lam dong','lang son','lao cai','long an','nam dinh','nghe an','ninh binh','ninh thuan','phu tho','phu yen','quang binh','quang nam','quang ngai','quang ninh','quang tri','soc trang','son la','tay ninh','thai binh','thai nguyen','thanh hoa','thua thien hue','tien giang','tra vinh','tuyen quang','vinh long','vinh phuc','yen bai']
#                     if self.text in cities:
#                         print(self.text)
#                         
#                     else: 
#                         print('khong hop le')
#                     
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
        
    def draw_game_guide(self,screen):
        screen.blit(game_guide,(90,90))
        
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



def main():
    clock = pygame.time.Clock()
    button_1 = Button(397,500,465,55,'Enter')
    button_2 = Button(30,10,35,35,'?')
    buttons = [button_1,button_2]
    input_box1 = InputBox(397,434,465,55)
    input_boxes = [input_box1]

    done = False
    ok = 0
    while not done:
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
                        
                    elif bt == buttons[1]:
                         bt.draw_game_guide(screen)
                      
                                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                
                    if (30 < mouse_x < 65) and (10 < mouse_y < 50):
                        ok = 1

                    else:
                        ok = 0
        
        screen.fill((255,255,255))
        for bt in buttons:
            bt.draw(screen)
        for box in input_boxes:
            box.draw(screen)
#         if ok == 1:
#             screen.blit(game_guide,(90,90))
#         
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()


