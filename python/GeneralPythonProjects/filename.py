import pygame

pygame.init()

window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Pygame Window")

# rect = pygame.Rect(100, 100, 100, 100)
# pygame.draw.rect(window, (255, 0, 0), rect, 10)

# center = (250, 250)
# radius = 50
# pygame.draw.circle(window, (0, 255, 0), center, radius)

# pygame.display.update()

color = [0, 0, 0]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                color = [0, 0, 0]     

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        color = [(1 + rgb) % 256 for rgb in color]
    if keys[pygame.K_r]:
        color[0] = (color[0] + 1) % 256
    if keys[pygame.K_g]:
        color[1] = (color[1] + 1) % 256
    if keys[pygame.K_b]:
        color[2] = (color[2] + 1) % 256
    window.fill(color)
    pygame.display.update()


pygame.quit()