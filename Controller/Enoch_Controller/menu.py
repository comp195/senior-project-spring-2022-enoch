import pygame
import serial
import time
import keyboard


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1920, 1080
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H), pygame.FULLSCREEN)
        self.font_name = 'Retro.ttf'
        self.titlefont_name = 'Tr2n.ttf'
        self.BLACK, self.WHITE, self.TRON = (0, 0, 0), (255, 255, 255), (97, 206, 235)
        self.main_menu = MainMenu(self)
        self.options = StationsMenu(self)
        self.credits = FreeModeMenu(self)
        self.curr_menu = self.main_menu


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_title_text(self, text, size, x, y ):
        font = pygame.font.Font(self.titlefont_name,size)
        text_surface = font.render(text, True, self.TRON)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(10, 10, 20, 20)
        self.offset = - 250

    def draw_cursor(self):
        self.game.draw_text('*', 100, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Options"
        # defining dimensions for each of the 3 state machines
        self.optionsx, self.optionsy = self.mid_w - 480, self.mid_h + 270
        self.creditsx, self.creditsy = self.mid_w + 480, self.mid_h + 270
        #starting position for our cursor
        self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            #this will set all of our flags for us
            self.game.check_events()
            #
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_title_text('ENOCH', 250, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Station Mode", 100, self.optionsx, self.optionsy)
            self.game.draw_text("Free Mode", 100, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        #handles when player presses the down key
        if self.game.DOWN_KEY:
            #if hovering over selected and down is pressed, move to options
            if self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            #if hovering over credits and down is pressed, move to start
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
        #handles when player presses the up key
        elif self.game.UP_KEY:
            if self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        #checks if the player wants to move the cursor
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class StationsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Station 1'
        self.station1x, self.station1y = self.mid_w, self.mid_h + 20
        self.station2x, self.station2y = self.mid_w, self.mid_h + 40
        self.station3x, self.station3y = self.mid_w, self.mid_h + 60
        self.station4x, self.station4y = self.mid_w, self.mid_h + 80
        self.station5x, self.station5y = self.mid_w + 480, self.mid_h + 405          
        self.cursor_rect.midtop = (self.station1x + self.offset, self.station1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            background = pygame.image.load('Enoch_Station_Mode.png')
            self.game.display.blit(background,(0,0))
            self.game.draw_text('Station Mode', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            #station 1
            self.game.draw_text("Station 1", 15, self.station1x, self.station1y)
            #station 2
            self.game.draw_text("Station 2", 15, self.station2x, self.station2y)
            #station 3
            self.game.draw_text("Station 3", 15, self.station3x, self.station3y)
            #station 4
            self.game.draw_text("Station 4", 15, self.station4x, self.station4y)
            self.game.draw_text("Connection Status:", 50, self.station5x, self.station5y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        #handles when player presses the down key
        if self.game.DOWN_KEY:
            #if hovering over selected and down is pressed, move to options
            if self.state == 'Station 1':
                self.cursor_rect.midtop = (self.station2x + self.offset, self.station2y)
                self.state = 'Station 2'
            #if hovering over options and down is pressed, move to credits
            elif self.state == 'Station 2':
                self.cursor_rect.midtop = (self.station3x + self.offset, self.station3y)
                self.state = 'Station 3'
            #if hovering over credits and down is pressed, move to start
            elif self.state == 'Station 3':
                self.cursor_rect.midtop = (self.station4x + self.offset, self.station4y)
                self.state = 'Station 4'
            #if hovering over credits and down is pressed, move to start
            elif self.state == 'Station 4':
                self.cursor_rect.midtop = (self.station1x + self.offset, self.station1y)
                self.state = 'Station 1'
        #handles when player presses the up key
        elif self.game.UP_KEY:
            if self.state == 'Station 1':
                self.cursor_rect.midtop = (self.station4x + self.offset, self.station4y)
                self.state = 'Station 4'
            elif self.state == 'Station 2':
                self.cursor_rect.midtop = (self.station1x + self.offset, self.station1y)
                self.state = 'Station 1'
            elif self.state == 'Station 3':
                self.cursor_rect.midtop = (self.station2x + self.offset, self.station2y)
                self.state = 'Station 2'
            elif self.state == 'Station 4':
                self.cursor_rect.midtop = (self.station3x + self.offset, self.station3y)
                self.state = 'Station 3'

    def check_input(self):
        #checks if the player wants to move the cursor
        self.move_cursor()
        if self.game.START_KEY:
            #if so, we're going to have to change to one of these state machines
            if self.state == 'Station 1':
                #self.game.playing = True
                print("Station 1 Test")
            elif self.state == 'Station 2':
                #self.game.curr_menu = self.game.options
                print("Station 2 Test")
            elif self.state == 'Station 3':
                #self.game.curr_menu = self.game.options
                print("Station 3 Test")
            elif self.state == 'Station 4':
                #self.game.curr_menu = self.game.credits
                print("Station 4 Test")
            self.run_display = False

"""
            background = pygame.image.load('Enoch_Free_Mode.png')
            self.game.display.blit(background,(0,0))
"""

class FreeModeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.station1x, self.station1y = self.mid_w, self.mid_h + 20
        self.station2x, self.station2y = self.mid_w, self.mid_h + 40
        self.station3x, self.station3y = self.mid_w, self.mid_h + 60
        self.station4x, self.station4y = self.mid_w + 480, self.mid_h + 405       
        self.cursor_rect.midtop = (self.station1x + self.offset, self.station1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            #self.check_input()
            background = pygame.image.load('Enoch_Free_Mode.png')
            self.game.display.blit(background,(0,0))
            self.game.draw_text("Connection Status:", 50, self.station4x, self.station4y)
            #self.draw_cursor()
            self.blit_screen()
            ser = serial.Serial('/dev/ttyACM0',115200, timeout=1)
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name == 't':
                    print('t was pressed\n')
                    ser.write(b"t\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'a':
                    print('a was pressed\n')
                    ser.write(b"a\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 's':
                    print('s was pressed\n')
                    ser.write(b"s\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'd':
                    print('d was pressed\n')
                    ser.write(b"d\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'f':
                    print('f was pressed\n')
                    ser.write(b"f\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'w':
                    print('w was pressed\n')
                    ser.write(b"w\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'e':
                    print('e was pressed\n')
                    ser.write(b"e\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'r':
                    print('r was pressed\n')
                    ser.write(b"r\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'i':
                    print('i was pressed\n')
                    ser.write(b"i\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'j':
                    print('j was pressed\n')
                    ser.write(b"j\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'm':
                    print('m was pressed\n')
                    ser.write(b"m\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'k':
                    print('k was pressed\n')
                    ser.write(b"k\n")
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'p':
                    print('quit was pressed\n')
                    quit()

#Game Execution
time.sleep(10)
g = Game()

while g.running:
    g.curr_menu.display_menu()