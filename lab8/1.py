import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((600, 800))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("rasist")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        column_width = SCREEN_WIDTH // 3  # Divide the screen width into 3 columns
        column = random.randint(0, 2)  # Randomly select a column (0, 1, or 2)
        self.rect.x = column * column_width + random.randint(0, column_width - self.rect.width)
        self.rect.y = random.randint(-self.rect.height * 2, -self.rect.height)
        self.speed = random.randint(1, 3)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        column_width = SCREEN_WIDTH // 3  # Divide the screen width into 3 columns
        column = random.randint(0, 2)  # Randomly select a column (0, 1, or 2)
        self.rect.x = column * column_width + random.randint(0, column_width - self.rect.width)
        self.rect.y = random.randint(-self.rect.height * 2, -self.rect.height)
        self.speed = random.randint(1, 3)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Create instances of Player, Enemy, and Coin
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Main game loop
collected_coins = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update player, enemy, and coin
    P1.update()
    E1.move()
    C1.move()

    # Check for collision between player and coin
    if pygame.sprite.collide_rect(P1, C1):
        collected_coins += 1
        C1.reset()

    # Check for collision between enemy and player
    if pygame.sprite.collide_rect(E1, P1):
        pygame.quit()
        sys.exit()

    # Draw everything
    DISPLAYSURF.fill(WHITE)
    all_sprites.draw(DISPLAYSURF)

    # Display collected coins
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Coins: {collected_coins}", True, BLACK)
    DISPLAYSURF.blit(text, (280, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)
