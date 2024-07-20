import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.get_default_font()
# white color 
color = (255,255,255) 
# light shade of the button 
color_light = (170,170,170) 
# dark shade of the button 
color_dark = (100,100,100) 
width = screen.get_width()
height = screen.get_height() 
smallfont = pygame.font.SysFont('Corbel',35) 
BotText = smallfont.render('bot' , True , color) 
PlayerText = smallfont.render('player', True, color)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
				
while running:			
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
               if 240 <= mouse[0] <= 240 + 140 and 340 <= mouse[1] <= 340 + 40:
                    pygame.quit()
               if 900 <= mouse[0] <= 900 + 140 and 340 <= mouse[1] <= 340 + 40:
                    pygame.quit()    
			
			#if the mouse is clicked on the 
			# button the game is terminated 
    screen.fill("purple")
    mouse = pygame.mouse.get_pos()
    screen.blit(BotText , (950,345))
    screen.blit(PlayerText , (270,345))
    if 900 <= mouse[0] <= 900 + 140 and 340 <= mouse[1] <= 340 + 40:
        pygame.draw.rect(screen,color_light,[900,340,140,40]) 
    else:
       pygame.draw.rect(screen,color_dark,[900,340,140,40])       
    if 240 <= mouse[0] <= 240 + 140 and 340 <= mouse[1] <= 340 + 40:
        pygame.draw.rect(screen,color_light,[240,340,140,40])
    else:
          pygame.draw.rect(screen,color_dark,[240,340,140,40])
    screen.blit(BotText , (950,345))
    screen.blit(PlayerText , (270,345))


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()