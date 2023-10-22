import pygame, Enemies,math


class Character(pygame.sprite.Sprite):
    def __init__(self, name, health,image_url,x,y):
        self.name = name
        self.health = health

        fist = Fist(5)
        self.inventory = Inventory()
        self.inventory.add_weapon(fist)
        self.selectedWeapon = fist

        self.image = pygame.image.load(image_url)
        self.scale = pygame.transform.scale(self.image, (40,40))
        self.rect = self.scale.get_rect()  
        self.rect.center = (x,y)

    def create_arrow(self):
        return Arrow(self.rect.x + 15 , self.rect.y + 17)

    def addWeapon(self, newWeapon):
        self.inventory.append(newWeapon)

    


    
    def spear(self, wep, surface):
        self.wep = wep
        self.scale = pygame.transform.scale(self.wep, (40,40))
        self.rect = self.scale.get_rect()
        surface.blit(self.scale, self.rect)


    def draw(self, surface):
        surface.blit(self.scale, self.rect)

    def moveChar(self,horz,vert):
        self.rect.x = self.rect.x + horz
        self.rect.y = self.rect.y + vert

    def collidesWith(self,collision):
        if self.rect.colliderect(collision.rect):
            return True
        else:
            return False
    def charRect(self):
        return self.rect
    def charPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y



class boy(Character):
    def __init__(self, name, health,x,y):
        super().__init__(name, health,"male.png",x,y)
        

        

class girl(Character):
    def __init__(self, name, health,x,y):
        super().__init__(name, health,"girl_char.png",x,y)
        

class Inventory(pygame.sprite.Sprite):
    def __init__(self, weapons=[]):
        self.weapons = weapons

    def add_weapon(self,newWeapon):
        self.weapons.append(newWeapon)
    def remove_weapon(self, weapon):
        self.weapons.remove(weapon)
    def find_weapon(self,weapon):
        for k in self.weapons:
            if weapon == k.name:
                return True
            else:
                return False


class Weapon(pygame.sprite.Sprite):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def draw(self, surface):
        surface.blit(self.scale, self.rect)


class Fist(Weapon):
    def __init__(self, damage):
        super().__init__("fist",damage)
class Spear(Weapon):
    def __init__(self, damage,image_url):
        super().__init__("Spear", damage)
        self.image = pygame.image.load(image_url)
    
        self.scale = pygame.transform.scale(self.image, (60,60))
        self.rect = self.scale.get_rect()
        self.rect.center = (475, 0)
class Axe(Weapon):
    def __init__(self, damage,image_url):
        super().__init__("axe", damage)
        self.image = pygame.image.load(image_url)
    
        self.scale = pygame.transform.scale(self.image, (20,20))
        self.rect = self.scale.get_rect()
class Bow(Weapon):
    def __init__(self,damage,image_url):
        super().__init__("bow", damage)
        self.image = pygame.image.load(image_url)
        self.scale = pygame.transform.scale(self.image, (20,20))
        self.rect = self.scale.get_rect()

    def shootArrow(self):
        #do nothing
        arrowSpeed = 10


class Katana(Weapon):
    def __init__(self, damage,image_url):
        super().__init__("katana", damage)
        self.image = pygame.image.load(image_url)
    
        self.scale = pygame.transform.scale(self.image, (20,20))
        self.rect = self.scale.get_rect()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("star.png")
        self.scale = pygame.transform.scale(self.image,(80, 80 ))
        self.rect = self.scale.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = pygame.math.Vector2(0, -1)  # default direction is up

    def update(self):
        self.rect.move_ip(self.speed * self.direction.x, self.speed * self.direction.y)
    def draw(self, surface):
        surface.blit(self.scale, self.rect)


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('arrow.png')
        self.image = pygame.transform.scale(self.image , (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center = (x, y))
        self.timer = 0
        self.start_time = pygame.time.get_ticks()


    def update(self):
        self.rect.x += 30





        
        
        




