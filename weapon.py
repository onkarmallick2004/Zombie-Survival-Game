from sprite_object import *

class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapons/shotgun/0 (1).png',  scale=0.4, animation_time=90, damage=50, tint=None, automatic=False):
        super().__init__(game=game, path=path,scale=scale, animation_time=animation_time)
        if tint:
            for i in range(len(self.images)):
                img = self.images[i]
                tint_surf = pg.Surface(img.get_size(), pg.SRCALPHA)
                tint_surf.fill(tint)
                img.blit(tint_surf, (0,0), special_flags=pg.BLEND_RGBA_MULT)
                
        self.images=deque(
            [pg.transform.smoothscale(img,(self.image.get_width()*scale,self.image.get_height()*scale))
             for img in self.images])
        self.weapon_pos=(HALF_WIDTH-self.images[0].get_width()//2,HEIGHT-self.images[0].get_height())
        self.reloading=False
        self.num_images=len(self.images)
        self.frame_counter=0
        self.damage=damage
        self.automatic=automatic

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot=False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image=self.images[0]
                self.frame_counter+=1
                if self.frame_counter==self.num_images:
                    self.reloading=False
                    self.frame_counter=0

    def draw(self):
        self.game.screen.blit(self.images[0],self.weapon_pos)

    def update(self):
       self.check_animation_time()
       self.animate_shot()

class Shotgun(Weapon):
    def __init__(self, game):
        super().__init__(game, damage=50, animation_time=90, automatic=False)

class Pistol(Weapon):
    def __init__(self, game):
        super().__init__(game, scale=0.3, damage=20, animation_time=50, automatic=False, tint=(100, 255, 100, 255))

class AssaultRifle(Weapon):
    def __init__(self, game):
        super().__init__(game, damage=35, animation_time=40, automatic=True, tint=(255, 100, 100, 255))
