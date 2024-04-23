import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255)) 
        self.rect = self.image.get_rect()
        self.rect.center = (320, 50) 
        self.speed = 0.2  
        self.dx = 0  
        self.dy = 0  

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.dy += 0.05

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))  
        self.image.fill((255, 255, 0)) 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 590)  
        self.rect.y = random.randint(50, 350)  

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Collect Squares")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.squares = pygame.sprite.Group()
        for _ in range(5): 
            square = Square()
            self.squares.add(square)
        self.game_over = False
        self.won = False

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.dx = -self.player.speed
            elif keys[pygame.K_RIGHT]:
                self.player.dx = self.player.speed
            else:
                self.player.dx = 0

            self.player.update()
            self.check_collisions()

            self.screen.fill((0, 0, 0))
            self.squares.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)

            pygame.display.flip()
            self.clock.tick(60)

    def check_collisions(self):
        # Check collisions with squares
        collisions = pygame.sprite.spritecollide(self.player, self.squares, True)
        if collisions:
            self.player.rect.center = (320, 50)  
            self.player.dy = 0 
            self.player.speed += 0.5  
            if len(self.squares) == 0: 
                self.won = True
                self.game_over = True

        if self.player.rect.bottom >= 480:
            self.game_over = True

if __name__ == "__main__":
    game = Game()
    game.run()
    if game.won:
        print("Congratulations! You collected all squares.")
    else:
        print("Game over! You hit the bottom without collecting all squares.")
