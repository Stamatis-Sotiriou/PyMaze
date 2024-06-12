from pygame import (sprite, draw, Rect, Surface, key, 
                    SRCALPHA, K_UP, K_DOWN, K_LEFT, K_RIGHT)
from random import choice, randint

class GameSprite(sprite.Sprite):
    def __init__(self, cor, size, color, speed = 0):
        self.x, self.y = cor[0], cor[1]
        self.size  = size
        self.color = color
        self.speed = speed
        
        self.rect = Rect(self.x, self.y, self.size[0], self.size[1])
        self.original_y = self.rect.y
        
        self.active = None
        
    def show(self, surface):
        draw.rect(surface, (self.color), ((self.rect.x, self.rect.y), (self.size)))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if (keys[K_UP] and self.rect.y > 20):
            self.rect.y -= self.speed 
        if (keys[K_DOWN] and self.rect.y < 430):
            self.rect.y += self.speed 
        if (keys[K_LEFT] and self.rect.x > 20):
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        
    def collision_check(self, wall):
        if self.rect.colliderect(wall):
            self.resolve_collision(wall)
            self.rect.x, self.rect.y = self.rect.topleft

    def resolve_collision(self, wall):
        if self.rect.right > wall.rect.left and self.rect.left < wall.rect.left:
            self.rect.right = wall.rect.left
        elif self.rect.left < wall.rect.right and self.rect.right > wall.rect.right:
            self.rect.left = wall.rect.right

        if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.top:
            self.rect.bottom = wall.rect.top
        elif self.rect.top < wall.rect.bottom and self.rect.bottom > wall.rect.bottom:
            self.rect.top = wall.rect.bottom

    def on_key(self, key):
        return self.rect.colliderect(key)
            

    def next_room(self):
        if self.rect.x <= 20:
            self.rect.x = 600
            return -1
        if self.rect.x >= 630:
            self.rect.x = 50
            return 1
        if self.rect.y <= 20:
            self.rect.y = 400
            return -4
        if self.rect.y >= 430:
            self.rect.y = 50
            return 4

class Wall(GameSprite):
    def wall_show(self, surface):
        if self.active:
            draw.rect(surface, (self.color), ((self.rect.x, self.rect.y), (self.size)))
        else:
            draw.rect(surface, (self.color), ((1500,0), (0,0)))

    def make_wall(surface, wall_list, active_list):
        for i in range(0,13,1):                
            cur_wall = wall_list[i]
            cur_wall.active = active_list[0][i]
            if cur_wall.active:
                cur_wall.wall_show(surface)

    def collision(wall_list, player):
        for wall in wall_list:
            if wall.active:
                player.collision_check(wall)

class Light():
    def __init__(self, cor):
        self.cor_choice = cor

    def init(self):
        self.size = (50, 50) 
        self.alpha_count = randint(90, 150)
		
        self.switch = True
        self.active = None
        
        self.small_rect = Surface((self.size), SRCALPHA)
        self.small_rect.set_alpha(self.alpha_count)
        self.small_rect.fill((255,255,0))

        self.mid_rect = Surface((self.size[0] * 1.5, self.size[1] * 1.5), SRCALPHA)
        self.mid_rect.set_alpha(self.alpha_count - 45)
        self.mid_rect.fill((255,200,0))

        self.big_rect = Surface((self.size[0] * 2, self.size[1] * 2), SRCALPHA)
        self.big_rect.set_alpha(self.alpha_count - 80)
        self.big_rect.fill((200,150,0))
    
    def get_new_cor(light_list):
        for light in light_list:
            light.x, light.y = choice(light.cor_choice)[0], choice(light.cor_choice)[1]
    
    def show(self, surface):
        surface.blit(self.small_rect, (self.x, self.y))
        surface.blit(self.mid_rect, (self.x - 12, self.y - 12))
        surface.blit(self.big_rect, (self.x - 25, self.y - 25))
    
    def update(self):
        if self.switch:
            self.alpha_count += 1
            self.small_rect.set_alpha(self.alpha_count)
            self.mid_rect.set_alpha(self.alpha_count - 45)
            self.big_rect.set_alpha(self.alpha_count - 80)
			
            if self.small_rect.get_alpha() > 180:
                self.switch = False
        else:
            self.alpha_count -= 1
            self.small_rect.set_alpha(self.alpha_count)
            self.mid_rect.set_alpha(self.alpha_count - 45)
            self.big_rect.set_alpha(self.alpha_count - 80)
			
            if self.small_rect.get_alpha() < 60:
                self.switch = True

    def make_lights(surface, light_list, active_list):
        for i in range(0,4,1):
            cur_light = light_list[i]
            cur_light.active = active_list[1][i]
        for light in light_list:
            if light.active:
                light.show(surface)
                light.update()
