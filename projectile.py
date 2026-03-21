import pygame as pg
import math
from sprite_object import SpriteObject

class Projectile(SpriteObject):
    def __init__(self, game, path, pos, angle, speed, damage):
        super().__init__(game, path, pos, scale=0.5, shift=0.5)
        self.angle = angle
        self.speed = speed
        self.damage = damage
        self.alive = True
    
    def update(self):
        super().update()
        if not self.alive:
            return
            
        dx = math.cos(self.angle) * self.speed * self.game.delta_time
        dy = math.sin(self.angle) * self.speed * self.game.delta_time
        self.x += dx
        self.y += dy
        
        # Check collision with wall
        if (int(self.x), int(self.y)) in self.game.map.world_map:
            self.alive = False
            return
            
        # Check collision with player
        player_dist = math.hypot(self.game.player.x - self.x, self.game.player.y - self.y)
        if player_dist < 0.5:
            self.alive = False
            self.game.player.get_damage(self.damage)
