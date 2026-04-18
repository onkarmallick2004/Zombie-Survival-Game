import pygame as pg
import math
from setting import *

class ObjectRenderer:
    def __init__(self,game):
        self.game=game
        self.screen=game.screen
        self.wall_textures=self.load_wall_textures()
        self.sky_image=self.get_texture('resources/textures/sky.png',(WIDTH,HALF_HEIGHT))
        self.sky_offset=0
        self.blood_screen=self.get_texture('resources/textures/blood_screen.png',RES)
        self.digit_size=90
        self.digit_images=[self.get_texture(f'resources/textures/digits/{i}.png',[self.digit_size]*2)
                           for i in range(11)]
        
        self.digits=dict(zip(map(str,range(11)),self.digit_images))
        self.game_over_image=self.get_texture('resources/textures/game_over.png',RES)
        self.win_image = self.get_texture('resources/textures/win.png', RES)

        self.win_image = self.get_texture('resources/textures/win.png', RES)
        self.zombie_font = pg.font.SysFont('Arial', 40)
        self.ammo_icon = self.get_texture('resources/sprites/static_sprites/ammo_crate.png', (30, 30))

    def draw_zombie_count(self):
        count = len([npc for npc in self.game.object_handler.npc_list if npc.alive])
        text = self.zombie_font.render(f'Wave: {self.game.object_handler.wave} | Zombies: {count}', True, (255, 255, 255))
        
        bg = pg.Surface((text.get_width() + 20, text.get_height() + 10))
        bg.set_alpha(150)
        bg.fill((0, 0, 0))
        
        pos_x = WIDTH - text.get_width() - 20
        pos_y = 20
        
        self.screen.blit(bg, (pos_x - 10, pos_y - 5))
        self.screen.blit(text, (pos_x, pos_y))

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()
        self.draw_weapon_ammo()
        self.draw_zombie_count()
        self.draw_minimap()

    def draw_weapon_ammo(self):
        weapon_name = type(self.game.weapon).__name__
        ammo_text = self.zombie_font.render(f'{weapon_name}: {self.game.weapon.ammo} / {self.game.weapon.max_ammo}', True, (255, 255, 0))
        
        icon_w, icon_h = self.ammo_icon.get_size()
        bg_w = ammo_text.get_width() + icon_w + 30
        bg_h = max(ammo_text.get_height(), icon_h) + 10
        
        bg = pg.Surface((bg_w, bg_h))
        bg.set_alpha(150)
        bg.fill((0, 0, 0))
        
        pos_x = WIDTH - bg_w - 20
        pos_y = HEIGHT - bg_h - 20
        
        self.screen.blit(bg, (pos_x, pos_y))
        self.screen.blit(self.ammo_icon, (pos_x + 10, pos_y + 5))
        self.screen.blit(ammo_text, (pos_x + 20 + icon_w, pos_y + 5))

    def draw_minimap(self):
        map_w = self.game.map.cols * 10
        map_h = self.game.map.rows * 10
        s = pg.Surface((map_w, map_h))
        s.set_alpha(150)
        s.fill((0, 0, 0))
        self.screen.blit(s, (10, 10))
        
        for x, y in self.game.map.world_map:
            pg.draw.rect(self.screen, (100, 100, 100), (10 + x * 10, 10 + y * 10, 10, 10))
            
        px, py = self.game.player.pos
        pg.draw.circle(self.screen, (0, 255, 0), (10 + int(px * 10), 10 + int(py * 10)), 3)
        
        length = 10
        end_x = int(px * 10) + math.cos(self.game.player.angle) * length
        end_y = int(py * 10) + math.sin(self.game.player.angle) * length
        pg.draw.line(self.screen, (255, 255, 0), (10 + int(px * 10), 10 + int(py * 10)), (10 + int(end_x), 10 + int(end_y)), 2)
    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def game_over(self):
        self.screen.blit(self.game_over_image,(0,0))

    def draw_player_health(self):
        health=str(self.game.player.health)
        
        bg = pg.Surface((len(health) * self.digit_size + self.digit_size, self.digit_size))
        bg.set_alpha(150)
        bg.fill((0, 0, 0))
        
        pos_y = HEIGHT - self.digit_size
        self.screen.blit(bg, (0, pos_y))
        
        for i,char in enumerate(health):
            self.screen.blit(self.digits[char],(i*self.digit_size, pos_y))
        self.screen.blit(self.digits['10'],((i+1)*self.digit_size, pos_y))

    def player_damage(self):
        self.screen.blit(self.blood_screen,(0,0))

    
    def draw_background(self):
        self.sky_offset=(self.sky_offset+4.5*self.game.player.rel)%WIDTH
        self.screen.blit(self.sky_image,(-self.sky_offset,0))
        self.screen.blit(self.sky_image,(-self.sky_offset+WIDTH,0))

        #floor
        pg.draw.rect(self.screen,FLOOR_COLOR,(0,HALF_HEIGHT,WIDTH,HEIGHT))



    def render_game_objects(self):
        list_objects=sorted(self.game.raycasting.objects_to_render,key=lambda t:t[0],reverse=True)
        for depth,image,pos in list_objects:
            self.screen.blit(image,pos)


    @staticmethod
    def get_texture(path,res=(TEXTURE_SIZE,TEXTURE_SIZE)):
        texture=pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture,res)
    
    def load_wall_textures(self):
        return{
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }
        