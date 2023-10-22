import pygame

class Background:
    def __init__(self, width, height, image_url):
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_url)
    
        self.scale = pygame.transform.scale(self.image, (1000,700))
        self.rect = self.scale.get_rect()

    def draw(self, surface):
        surface.blit(self.scale, self.rect)


class LevelBackground(Background):
    def __init__(self, width, height, image_url):
        super().__init__(width, height, image_url)

    def delete(self):
        del self


