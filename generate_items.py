import pygame as pg

pg.init()

# Health Pack
surf = pg.Surface((64, 64), pg.SRCALPHA)
pg.draw.rect(surf, (200, 200, 200), (8, 16, 48, 32))
pg.draw.rect(surf, (255, 0, 0), (28, 20, 8, 24))
pg.draw.rect(surf, (255, 0, 0), (20, 28, 24, 8))
pg.image.save(surf, "resources/sprites/static_sprites/health_pack.png")

# Ammo Crate
surf2 = pg.Surface((64, 64), pg.SRCALPHA)
pg.draw.rect(surf2, (0, 100, 0), (8, 16, 48, 32))
pg.draw.rect(surf2, (200, 200, 0), (16, 24, 16, 16))
pg.draw.rect(surf2, (200, 200, 0), (32, 24, 16, 16))
pg.image.save(surf2, "resources/sprites/static_sprites/ammo_crate.png")
