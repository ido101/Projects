import pygame
import random

pygame.init()
window_width = 800
window_height = 640
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("BasketBall")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 26)
score = 0

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

basket_width = 150
basket_height = 50
basket_x = (window_width - basket_width) / 2
basket_y = window_height - basket_height
basket_movement = 10

radius_ball = 36
ball_x = random.randint(radius_ball, window_width - radius_ball)
ball_y = 0

current_streak = 0
best_streak = 0

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_movement
    if keys[pygame.K_RIGHT] and basket_x < window_width - basket_width:
        basket_x += basket_movement
        
    ball_y += 8
    if ball_y > window_height:
        ball_x = random.randint(radius_ball, window_width - radius_ball)
        ball_y = 0
        score -= 1
        current_streak = 0
    
    if ball_y + radius_ball > basket_y and ball_x > basket_x and ball_x < basket_x + basket_width:
        ball_x = random.randint(radius_ball, window_width - radius_ball)
        ball_y = 0
        score += 1
        current_streak += 1
        if current_streak > best_streak:
            best_streak = current_streak
            
    window.fill(white)
    score_text = font.render("Score: " + str(score), True, black)
    current_streak_text = font.render("Current Streak: " + str(current_streak), True, black)
    best_streak_text = font.render("Best Streak: " + str(best_streak), True, black)
    window.blit(score_text, (10 , 10))
    window.blit(current_streak_text, (130 , 10))
    window.blit(best_streak_text, (350 , 10))
    pygame.draw.rect(window, black, [basket_x, basket_y, basket_width, basket_height])
    pygame.draw.circle(window, red, (ball_x, ball_y), radius_ball)
    pygame.display.update()

pygame.quit() 
exit()