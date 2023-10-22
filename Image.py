import pygame
class image(pygame.sprite.Sprite):
    def __init__(self,x,y,img_path, xscale, yscale):
        self.image = pygame.image.load(img_path)
        self.scale = pygame.transform.scale(self.image, (xscale, yscale))
        self.scale.set_colorkey((255,255,255))
        self.rect = self.scale.get_rect()  
        self.rect.center = x,y

    def collidesWith(self,collision):
        if self.rect.colliderect(collision.rect):
            return True
        else:
            return False
        
    def draw(self, surface):
        surface.blit(self.scale, self.rect)
    