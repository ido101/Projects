import pygame
import random

window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Shooter")
icon_image = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(icon_image)

score = 0
score_x = 10
score_y = 10
# font = pygame.font.SysFont("Arial", 26)

space_ship = pygame.image.load("Assets/player.png")
ship_x = (window_width - space_ship.get_rect().width) / 2
ship_y = window_height - space_ship.get_rect().height - 20
ship_movement = 1

enemy = pygame.image.load("Assets/enemyShip.png")
enemy_x = random.randint(enemy.get_rect().width, window_width - enemy.get_rect().width)
enemy_y = random.randint(enemy.get_rect().height + 50, 500)
enemy_movement = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 0:
        ship_x -= ship_movement
    if keys[pygame.K_RIGHT] and ship_x < window_width - space_ship.get_rect().width:
        ship_x += ship_movement
    window.fill("black")
    window.blit(space_ship, (ship_x, ship_y))
    window.blit(enemy, (enemy_x, enemy_y))
    pygame.display.update()

pygame.quit()
exit()