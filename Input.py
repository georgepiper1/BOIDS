import pygame
from Variables import *

class InputBox:

    def __init__(self, x, y, w, h,inp, font,text=''):
        
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.value=inp

    def handle_event(self, event,font):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.value=self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)


    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen, Boxon):
        if Boxon==True:
            # Blit the text.
            screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
            # Blit the rect.
            pygame.draw.rect(screen, self.color, self.rect, 2)
            
class Button():
    
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)                                         
        self.image = pygame.image.load("Cogwheel.png")
        self.rect = self.image.get_rect()
        self.rect.center=(1350,800)
        
        self.activate=False
        
    def handle_event(self, event):
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.activate==False:
                    self.activate=True
                else:
                    self.activate=False
    
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',18)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)