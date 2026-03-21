import pygame as pg
import sys
from setting import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import*
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(True)
        self.screen=pg.display.set_mode(RES)
        self.clock=pg.time.Clock()
        self.delta_time=1
        self.global_trigger=False
        self.global_event=pg.USEREVENT+0
        pg.time.set_timer(self.global_event,40)
        self.state = 'START_MENU'
        self.difficulty = 1
        self.new_game()

    def new_game(self):
        self.map=Map(self)
        self.player=Player(self)
        self.object_renderer=ObjectRenderer(self)
        self.raycasting=RayCasting(self)
        self.object_handler=ObjectHandler(self)
        self.weapon=Weapon(self)
        self.sound=Sound(self)
        self.pathfinding=PathFinding(self)
        pg.mixer.music.play(-1)

    def draw_text(self, text, size, color, x, y):
        font = pg.font.SysFont('Arial', size)
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.blit(surface, rect)
        return rect
        
    def start_playing(self):
        self.state = 'PLAYING'
        pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        pg.mouse.get_rel()
        pg.mouse.set_visible(False)
        if hasattr(pg.event, 'set_grab'):
            pg.event.set_grab(True)

    def draw_start_menu(self):
        self.screen.fill('black')
        self.draw_text("ZOMBIE SHOOTER", 80, (255, 0, 0), HALF_WIDTH, HALF_HEIGHT - 100)
        self.btn_easy = self.draw_text("EASY", 40, (0, 255, 0), HALF_WIDTH, HALF_HEIGHT)
        self.btn_medium = self.draw_text("MEDIUM", 40, (255, 255, 0), HALF_WIDTH, HALF_HEIGHT + 60)
        self.btn_hard = self.draw_text("HARD", 40, (255, 0, 0), HALF_WIDTH, HALF_HEIGHT + 120)

    def draw_pause_menu(self):
        s = pg.Surface((WIDTH, HEIGHT))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        self.screen.blit(s, (0,0))
        self.draw_text("PAUSED", 80, (255, 255, 255), HALF_WIDTH, HALF_HEIGHT - 100)
        self.btn_resume = self.draw_text("RESUME", 50, (255, 255, 255), HALF_WIDTH, HALF_HEIGHT)
        self.btn_exit = self.draw_text("EXIT", 50, (255, 255, 255), HALF_WIDTH, HALF_HEIGHT + 100)

    def update(self):
        if self.state == 'PLAYING':
            self.player.update()
            self.raycasting.update()
            self.object_handler.update()
            self.weapon.update()
        pg.display.flip()
        self.delta_time=self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        if self.state in ('PLAYING', 'PAUSED'):
            self.object_renderer.draw()
            self.weapon.draw()
            if self.state == 'PAUSED':
                self.draw_pause_menu()
        elif self.state == 'START_MENU':
            self.draw_start_menu()

    def check_events(self):
        self.global_event=False
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type==pg.KEYDOWN and event.key == pg.K_ESCAPE:
                if self.state == 'PLAYING':
                    self.state = 'PAUSED'
                    pg.mouse.set_visible(True)
                    if hasattr(pg.event, 'set_grab'):
                        pg.event.set_grab(False)
                elif self.state == 'PAUSED':
                    self.start_playing()
            elif event.type==self.global_event:
                self.global_trigger=True

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.state == 'START_MENU':
                    if hasattr(self, 'btn_easy') and self.btn_easy.collidepoint(event.pos):
                        self.difficulty = 1
                        self.new_game()
                        self.start_playing()
                    if hasattr(self, 'btn_medium') and self.btn_medium.collidepoint(event.pos):
                        self.difficulty = 2
                        self.new_game()
                        self.start_playing()
                    if hasattr(self, 'btn_hard') and self.btn_hard.collidepoint(event.pos):
                        self.difficulty = 3
                        self.new_game()
                        self.start_playing()
                elif self.state == 'PAUSED':
                    if hasattr(self, 'btn_resume') and self.btn_resume.collidepoint(event.pos):
                        self.start_playing()
                    if hasattr(self, 'btn_exit') and self.btn_exit.collidepoint(event.pos):
                        pg.quit()
                        sys.exit()

            if self.state == 'PLAYING':
                self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__=='__main__':
    game=Game()
    game.run()

