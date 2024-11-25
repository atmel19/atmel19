# Traffic Rider - Python Game
# Pygame asosida yaratilgan mototsikl simulyatori

import pygame
import random
import sys

# O'yin parametrlari
WIDTH, HEIGHT = 400, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Pygame sozlash
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Rider")
clock = pygame.time.Clock()

# O'yinchi klassi
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 150))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# To'siqlar klassi
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 100))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), -100))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = -100
            self.rect.x = random.randint(50, WIDTH - 50)

# Sprite guruhlari
player = Player()
obstacles = pygame.sprite.Group(Obstacle() for _ in range(5))
all_sprites = pygame.sprite.Group(player, *obstacles)

# O'yin tsikli
def main():
    """Traffic Rider o'yini"""
    running = True
    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Yangilash
        all_sprites.update(keys)
        
        # To'qnashuvni tekshirish
        if pygame.sprite.spritecollide(player, obstacles, False):
            print("GAME OVER")
            running = False

        # Chizish
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    # Loyiha haqida README matni
    print("Traffic Rider - Pygame o'yini")
    print(">> O'yinchi mototsiklni boshqarib, to'siqlardan qochadi.")
    print(">> Chapga va o'ngga harakatlanish uchun LEFT/RIGHT tugmalarini bosing.")
    print(">> To'qnashuv yuz berganda o'yin tugaydi.")
    print("\nBoshqa ma'lumotlar:")
    print("- Python: 3.9 yoki undan yuqori")
    print("- Pygame: 2.1.2")
    print("- Loyiha muallifi: Sizning ismingiz")
    print("\nBoshlash uchun o'yinni yuklab oling va Pygame kutubxonasini o'rnating.")
    print("Qo'shimcha: `pip install pygame` buyrug'ini ishlating.\n")
    print("O'yin ishga tushmoqda...")
    
    main()
