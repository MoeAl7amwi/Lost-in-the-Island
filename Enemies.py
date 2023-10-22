import pygame,math, random, time
from pygame.sprite import Sprite,Group
import Character



class Enemies (pygame.sprite.Sprite):
    def __init__(self, health,width,height,image_url):
        self.health = health
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_url)
    
        self.scale = pygame.transform.scale(self.image,(width,height))
        self.rect = self.scale.get_rect()
    def draw(self, surface):
        surface.blit(self.scale, self.rect)
class Enemies2 (pygame.sprite.Sprite):
    def __init__(self, health,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.width = width
        self.height = height
    
    def draw(self, surface):
        surface.blit(self.scale, self.rect)

class Spider(pygame.sprite.Sprite):
    def __init__(self, x, y, all_sprites, web_group):
        super().__init__()
        self.animation_frames = [
        pygame.image.load("spider1.png"),
        pygame.image.load("spider2.png"),
        pygame.image.load("spider3.png"),
        ]

        self.current_frame = 0
        self.animation_speed = 7
        self.animation_counter = 0

        self.image = self.animation_frames[self.current_frame]
        self.scale = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.scale.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 15
        self.web_timer = 0
        self.web_cooldown = 150000
        self.all_sprites = all_sprites
        self.web_group = web_group
    def update(self, screen_height):
        self.rect.x += self.speed
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.current_frame]
            self.scale = pygame.transform.scale(self.image, (300, 200))
            self.animation_counter = 0
        if self.rect.right > pygame.display.get_surface().get_rect().right or self.rect.left < 0:
            self.speed = -self.speed
        self.web_timer += pygame.time.get_ticks()
        if self.web_timer >= self.web_cooldown:
            self.web_timer = 0
            web = Web(self.rect.centerx, self.rect.centery)
            self.all_sprites.add(web)
            self.web_group.add(web)
        for web in self.web_group:
            if web.rect.top >= screen_height:
                web.kill()
class Web(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('web.png')
        self.image = pygame.transform.scale(self.image , (100, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(5, 15)
    def update(self, *args, **kwargs):
        self.rect.y += self.speed  

class Centipede (pygame.sprite.Sprite): 
    def __init__(self, x,y,all_sprites,slime_group):
        super().__init__()
        self.image = pygame.image.load("centipede.png")
        self.scaled = pygame.transform.scale(self.image,(300,200))
        self.rect=self.scaled.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moveSpeed = 20
        self.slime_time = 0
        self.all_sprites = all_sprites
        self.slime_group = slime_group
    def update(self,screen_top):
        self.rect.x+=self.moveSpeed
        if self.rect.right > pygame.display.get_surface().get_rect().right or self.rect.left < 0:
            self.moveSpeed = -self.moveSpeed
            self.rect.y = random.randrange(-100,300)

        self.slime_time+= pygame.time.get_ticks()
        if self.slime_time >= 200000:
            self.slime_time = 0
            slime = slimeBall(self.rect.centerx, self.rect.bottom,random.randrange(6,12),True)
            self.all_sprites.add(slime)
            self.slime_group.add(slime)
        for slime in self.slime_group:
            if slime.rect.top >= screen_top:
                slime.kill() 

class slimeBall(pygame.sprite.Sprite):
    def __init__(self,x,y,speed,switch):
        super().__init__()
        self.image = pygame.image.load('slime.png')
        self.slime = pygame.transform.scale(self.image,(100, 75))
        self.rect = self.slime.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
        self.switch=True
    def update(self, *args, **kwargs):
        self.rect.y += self.speed
        if(self.switch):
         self.rect.x +=self.speed 
         self.switch=False
        else:
            self.rect.x+=-self.speed
            self.switch=True
    

class Dragon (Enemies2): 
    def __init__(self, width,height,health):
        super().__init__(width,height,health)
        self.width = width
        self.height = height
        #self.image = pygame.image.load(image_url)

        katana = Character.Katana(30,"katana.png")
        self.drop = katana
    

        self.animation_frames = [
        pygame.image.load("dragon1.png"),
        pygame.image.load("dragon2.png"),
        pygame.image.load("dragon3.png"),
        ]

        self.current_frame = 0
        self.animation_speed = 10
        self.animation_counter = 0

        self.image = self.animation_frames[self.current_frame]
        self.scale = pygame.transform.scale(self.image, (width, height))
        self.rect = self.scale.get_rect()
        self.health = health

        

    def dropLoot(self,x,y):
        #if the enemy dies this will drop their weapon for the user
        item = self.drop

        item.rect.x = x
        item.rect.y = y


    def create_fire_sprites(self,x,y,numsprites):
        fire_group = pygame.sprite.Group()
        for i in range(numsprites):
            sprite = FireSprite(x,y)
            fire_group.add(sprite)
        return fire_group
    
    def update(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.current_frame]
            self.scale = pygame.transform.scale(self.image, (self.width, self.height))
            self.animation_counter = 0




class FireSprite(pygame.sprite.Sprite):
            def __init__(self,xpos,ypos):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("fireball.png")
                self.scale = pygame.transform.scale(self.image,(40, 40))
                self.rect = self.scale.get_rect()
                self.rect.x = xpos
                self.rect.y = ypos
                self.speed = random.randint(-15,15)
                rand = random.randint(0,200)

            def move(self,speedx,speedy):
                self.rect.x += speedx
                self.rect.y += speedy


class FinalBoss (Enemies): 
    def __init__(self, width, height, health, image_url):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(width,height, health, image_url)
        self.health = health
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_url)
        self.scale = pygame.transform.scale(self.image, (width,height))
        self.rect = self.scale.get_rect()
    def teleport(self, screen_width, screen_height):
        x = random.randint(100, screen_width - 100)
        y = random.randint(65, screen_height)
        self.rect.x = x
        self.rect.y = y
        time.sleep(0.05)
    def create_bullet(self):
        return MagicBall(self.rect.x + 15 , self.rect.y + 17)

class MagicBall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('magicBall.png')
        self.image = pygame.transform.scale(self.image , (100, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center = (x, y))
        self.timer = 0
        self.start_time = pygame.time.get_ticks()


    def update(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        self.rect.x -= 5
        
        #if self.timer >= 0:
            #self.kill()



       
    
    
    

