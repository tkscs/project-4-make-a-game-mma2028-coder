import random
import pygame
pygame.init()
player = pygame.Rect(320,240,50,50)
WIDTH, HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
coin = pygame.Rect(random.randint(0, WIDTH-20), random.randint(0, HEIGHT-20), 20, 20)
speed = 5
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
    pygame.draw.rect(screen, (255,0,0), (player.x, player.y, 50, 50))
    pygame.draw.rect(screen, (255,255,0), coin)
    pygame.display.update()

    if player.colliderect(coin):
        coin.x = random.randint(0, WIDTH-20)
        coin.y = random.randint(0, HEIGHT-20)

pygame.quit()