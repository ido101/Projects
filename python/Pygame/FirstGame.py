import pygame

pygame.init()
window_width = 800
window_height = 640
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Game")
 

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player_width = 50
player_height = 50
player_x = (window_width - player_width) // 2
player_y = (window_height - player_height) // 2
player_movement = 1
player_color = red
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= player_movement
    if keys[pygame.K_RIGHT] and player_rect.x < window_width - player_width:
        player_rect.x += player_movement
    if keys[pygame.K_DOWN] and player_rect.y < window_height - player_height:
        player_rect.y += player_movement
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= player_movement

    window.fill(white)
    pygame.draw.rect(window, player_color, player_rect)
    pygame.display.update()


pygame.quit()