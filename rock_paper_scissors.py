import pygame
import sys
import random
from funclib import determine_winner

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.get_default_font()
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100) 
width = screen.get_width()
height = screen.get_height() 
smallfont = pygame.font.SysFont('Corbel',35) 
BotText = smallfont.render('bot' , True , color) 
PlayerText = smallfont.render('player', True, color)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
home = True
screen.fill("purple")
rocktext = smallfont.render('rock', True, color)
papertext = smallfont.render('paper', True, color)
scissorrext = smallfont.render('scissor', True, color)
tie = smallfont.render('Its a tie!', True, color)
botwin = smallfont.render('Bot wins!', True, color)
playerwin = smallfont.render('Player wins!', True, color)
playerpick = None


while running:	
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
          
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 240 <= mouse[0] <= 240 + 140 and 340 <= mouse[1] <= 340 + 40:
                pygame.quit()
            if 900 <= mouse[0] <= 900 + 140 and 340 <= mouse[1] <= 340 + 40:
                screen.fill("purple")
                x = random.choice(["rock", "paper", "scissor"])
                print(x)
                home = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 240 <= mouse[0] <= 240 + 140 and 140 <= mouse[1] <= 140 + 40:
                    playerpick = "rock"
                if 900 <= mouse[0] <= 900 + 140 and 140 <= mouse[1] <= 140 + 40:
                    playerpick = "scissor"  
                if 580 <= mouse[0] <= 580 + 140 and 140 <= mouse[1] <= 140 + 40:
                    playerpick = "paper"
                if playerpick is not None:
                    winner = determine_winner(playerpick, x)
                    screen.blit(smallfont.render(winner, True, color), (580,290))
        if event.type == pygame.quit:
            pygame.quit()
    screen.fill("purple")         
    pygame.draw.rect(screen,color_dark, [900, 140, 140, 40])
    screen.blit(scissorrext, (900, 140))
    pygame.draw.rect(screen,color_dark, [240, 140, 140, 40])
    screen.blit(rocktext, (270, 140))
    pygame.draw.rect(screen, color_dark, [580,140,140,40])
    screen.blit(papertext, (580,140))
    if event.type == pygame.MOUSEBUTTONDOWN:
                if 240 <= mouse[0] <= 240 + 140 and 140 <= mouse[1] <= 140 + 40:
                    playerpick = "rock"
                if 900 <= mouse[0] <= 900 + 140 and 140 <= mouse[1] <= 140 + 40:
                    playerpick = "scissor"  
                if 580 <= mouse[0] <= 580 + 140 and 140 <= mouse[1] <= 140 + 40:
                    playerpick = "paper"
                if playerpick is not None:
                    winner = determine_winner(playerpick, x)
                    screen.blit(smallfont.render(winner, True, color), (580,290))
                    
                       

    if home == True:   
            screen.fill("purple")            
            if event.type == pygame.QUIT: 
                running = False    
            if 900 <= mouse[0] <= 900 + 140 and 340 <= mouse[1] <= 340 + 40:
                pygame.draw.rect(screen,color_light,[900,340,140,40]) 
                screen.blit(BotText, (950,345))
            else:
                pygame.draw.rect(screen,color_dark,[900,340,140,40]) 
                screen.blit(BotText , (950,345))      
            if 240 <= mouse[0] <= 240 + 140 and 340 <= mouse[1] <= 340 + 40:
                pygame.draw.rect(screen,color_light,[240,340,140,40])
                screen.blit(PlayerText , (270,345))
            else:
                pygame.draw.rect(screen,color_dark,[240,340,140,40])
                screen.blit(PlayerText , (270,345))



    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()