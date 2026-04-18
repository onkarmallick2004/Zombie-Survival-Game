import pygame as pg
import math
from sprite_object import SpriteObject

class Item(SpriteObject):
    def __init__(self, game, path, pos, scale=0.4, shift=0.2):
        super().__init__(game=game, path=path, pos=pos, scale=scale, shift=shift)
        self.alive = True

    def check_pickup(self):
        px, py = self.game.player.pos
        if math.hypot(self.x - px, self.y - py) < 0.6:
            self.apply_effect()
            self.alive = False

    def apply_effect(self):
        pass

    def update(self):
        if self.alive:
            self.check_pickup()
            super().update()

class HealthPack(Item):
    def __init__(self, game, pos):
        super().__init__(game, path='resources/sprites/static_sprites/health_pack.png', pos=pos)
        
    def apply_effect(self):
        from setting import PLAYER_MAX_HEALTH
        self.game.player.health = min(PLAYER_MAX_HEALTH, self.game.player.health + 50)

class AmmoCrate(Item):
    def __init__(self, game, pos):
        super().__init__(game, path='resources/sprites/static_sprites/ammo_crate.png', pos=pos)
        
    def apply_effect(self):
        for weapon in self.game.weapons:
            weapon.ammo = weapon.max_ammo
