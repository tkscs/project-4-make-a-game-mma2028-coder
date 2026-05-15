import random
import pygame
pygame.init()
pygame.mixer.init()
coin_sound = pygame.mixer.Sound("coin.wav")
fruit_sound = pygame.mixer.Sound("/Users/matthewma/Downloads/squarebun-apple-bite-316785.wav")
player = pygame.Rect(320,240,50,50)
WIDTH, HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
coin = pygame.Rect(random.randint(0, WIDTH-20), random.randint(20, HEIGHT-20), 24, 24)
fruit = pygame.Rect(random.randint(0, WIDTH-30), random.randint(20,HEIGHT-30),30,20)
speed = 3
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), player)
    pygame.draw.circle(screen, (120,80,0), coin.center,14)
    pygame.draw.circle(screen, (255,215,0),coin.center,12)
    pygame.draw.circle(screen, (255,255,180), (coin.centerx - 4, coin.centery - 4), 4)
    pygame.display.update()

    pygame.draw.rect(screen, (255,0,0), player)
    pygame.draw.circle(screen, (120,80,0), fruit.center,14)
    pygame.draw.circle(screen, (255,215,0),fruit.center,12)
    pygame.draw.circle(screen, (255,255,180), (fruit.centerx - 4, fruit.centery - 4), 4)
    pygame.display.update()

    if player.colliderect(coin):
        coin_sound.play()
        coin.x = random.randint(0, WIDTH-20)
        coin.y = random.randint(0, HEIGHT-20)
    if player.colliderect(fruit):
        fruit_sound.play()
        fruit.x = random.randint(0, WIDTH-20)
        fruit.y = random.randint(0, HEIGHT-20)

pygame.quit()