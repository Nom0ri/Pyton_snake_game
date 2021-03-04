import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#window size
win_y = 600
win_x = 800
window=pygame.display.set_mode((win_x,win_y))
pygame.display.update()

pygame.display.set_caption('Pyton by Nomori')

snek_size = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("comicsansms", 40)
score_style = pygame.font.SysFont("comicsansms", 35)

def show_score(score):
    value = score_style.render("Score: " + str(score), True, white)
    window.blit(value, [0, 0])

def snek(snek_size, snek_list):
    for x in snek_list:
        pygame.draw.rect(window, white, [x[0], x[1], snek_size, snek_size])

def message(msg,color):
    text = font_style.render(msg, True, color)
    window.blit(text, [win_x/4,win_y/2])

def game():  #Main game function
    game_over = False
    game_close = False

    x1 = win_x/2
    y1 = win_y/2
    x1_upd = 0       
    y1_upd = 0

    foodx = round(random.randrange(0, win_x - snek_size) / 10.0) * 10.0
    foody = round(random.randrange(0, win_y - snek_size) / 10.0) * 10.0

    snek_list=[]
    snek_len=1
    while not game_over:
        while game_close == True:
            window.fill(black)
            message("Q - exit or E - try again", white)
            show_score(snek_len-1)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type==pygame.QUIT: #React to close button
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_e:
                        game()

        for event in pygame.event.get():
            if event.type==pygame.QUIT: #React to close button
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_upd = -snek_size
                    y1_upd = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_upd = snek_size
                    y1_upd = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_upd = -snek_size
                    x1_upd = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_upd = snek_size
                    x1_upd = 0

        if x1 >= win_x or x1 < 0 or y1 >= win_y or y1 < 0:
            game_close = True

        x1 += x1_upd
        y1 += y1_upd
        window.fill(black)

        #set snake speed
        speed = 15        
        clock = pygame.time.Clock()
        clock.tick(speed)

        pygame.draw.rect(window, red, [foodx, foody, snek_size, snek_size])
        snek_head = []
        snek_head.append(x1)
        snek_head.append(y1)
        snek_list.append(snek_head)
        if len(snek_list) > snek_len:
            del snek_list[0]
 
        for x in snek_list[:-1]:
            if x == snek_head:
                game_close = True
 
        snek(snek_size, snek_list)
        show_score(snek_len-1)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_x - snek_size) / 10.0) * 10.0
            foody = round(random.randrange(0, win_y - snek_size) / 10.0) * 10.0
            snek_len += 1
        pygame.display.update()

    pygame.quit()
    quit()

game()