from sprite_object import *
from npc import *
from random import choices, randrange
from items import HealthPack, AmmoCrate

class ObjectHandler:
    def __init__(self,game):
        self.game=game
        self.sprite_list=[]
        self.npc_list=[]
        self.npc_sprite_path='resources/sprites/npc/'
        self.static_sprite_path='resources/sprites/static_sprites/'
        self.anim_sprite_path='resources/sprites/animated_sprites/'
        add_sprite=self.add_sprite
        add_npc=self.add_npc
        self.npc_positions={}
        self.wave = 1

         # spawn npc
        f = getattr(game, 'difficulty', 1)
        self.enemies = 20 * (f**2)  # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC, MaleZombieNPC,IndustrialZombieNPC,FemaleZombieNPC]
        self.weights = [0, 0, 0,70,50,50]
        self.restricted_area = {(i, j) for i in range(10 * f) for j in range(10 * f)}
        self.spawn_npc()
        self.spawn_items()

        add_sprite(AnimatedSprite(game, pos=(11.5 * f, 3.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(1.5 * f, 1.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(1.5 * f, 7.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(5.5 * f, 3.25 * f)))
        add_sprite(AnimatedSprite(game, pos=(5.5 * f, 4.75 * f)))
        add_sprite(AnimatedSprite(game, pos=(7.5 * f, 2.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(7.5 * f, 5.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(14.5 * f, 1.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(14.5 * f, 4.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5 * f, 5.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5 * f, 7.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5 * f, 7.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5 * f, 7.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5 * f, 12.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5 * f, 20.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(10.5 * f, 20.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5 * f, 14.5 * f)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5 * f, 18.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(14.5 * f, 24.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(14.5 * f, 30.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(1.5 * f, 30.5 * f)))
        add_sprite(AnimatedSprite(game, pos=(1.5 * f, 24.5 * f)))

    def spawn_items(self):
        f = getattr(self.game, 'difficulty', 1)
        for _ in range(10 * f):
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_sprite(HealthPack(self.game, pos=(x + 0.5, y + 0.5)))
            
        for _ in range(10 * f):
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_sprite(AmmoCrate(self.game, pos=(x + 0.5, y + 0.5)))


    def spawn_npc(self):
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))


    def check_win(self):
        if not any(npc.alive for npc in self.npc_list):
            self.wave += 1
            f = getattr(self.game, 'difficulty', 1)
            self.enemies = int(20 * (f**2) * (1.2 ** self.wave))
            # Increase weights for harder enemies
            self.weights = [self.weights[0]+2, self.weights[1]+1, self.weights[2]+1, self.weights[3], self.weights[4], self.weights[5]]
            self.spawn_npc()
            self.spawn_items()
        


    def update(self):
        self.npc_positions={npc.map_pos for npc in self.npc_list if npc.alive}
        self.sprite_list = [sprite for sprite in self.sprite_list if getattr(sprite, 'alive', True)]
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()


    def add_npc(self,npc):
        self.npc_list.append(npc)



    def add_sprite(self,sprite):
        self.sprite_list.append(sprite)