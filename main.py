#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: Alice 'Ava' Williams
Date: July 26, 2021
File: main.py
Desc: Entry point and main loop for application.
"""

#Imports
import pygame
import game

def main():

    #Initialization
    pygame.init()
    surface = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
    pygame.display.set_caption(game.TITLE)
    clock = pygame.time.Clock()
    gameObj = game.Game()
    cells = gameObj.init_cells(int(game.WIDTH / game.DIM), int(game.HEIGHT / game.DIM))
    
    #Controls Information
    print("Controls:\n\tLeft click -- toggle tile state while paused\n\tspacebar -- start or pause the game\n\ts -- save to file\n\tl -- load from file (gen# doesn't save)\n\tr -- restarts game\n\tesc -- quits the game")

    #Runtime Flags
    running = True
    paused = True
    
    #Generation Count
    gen = 0
    font = pygame.font.SysFont('arial', 28)
    #print(pygame.font.get_fonts()) #Print fonts found
    
    #Initial Draw
    gameObj.draw_grid(surface, cells)
    gameObj.draw_gen(font, surface, gen)
    pygame.display.update()
    
    #Main Loop
    while running:
        
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
                    continue
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                        continue
                    elif event.key == pygame.K_s:
                        gameObj.save_grid(cells)
                        continue
                    elif event.key == pygame.K_l:
                        cells = gameObj.load_grid()
                        gameObj.draw_grid(surface, cells)
                        gen = 0
                        gameObj.draw_gen(font, surface, gen)
                        pygame.display.update()
                        continue
                    elif event.key == pygame.K_r:
                        print("Resetting the game state...")
                        cells = gameObj.init_cells(int(game.WIDTH / game.DIM), int(game.HEIGHT / game.DIM))
                        gen = 0
                        gameObj.draw_grid(surface, cells)
                        gameObj.draw_gen(font, surface, gen)
                        pygame.display.update()
                        continue
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        paused = False
                        continue
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        cells[int(pygame.mouse.get_pos()[1]/game.DIM), int(pygame.mouse.get_pos()[0]/game.DIM)] = not cells[int(pygame.mouse.get_pos()[1]/game.DIM), int(pygame.mouse.get_pos()[0]/game.DIM)]
                        gameObj.draw_grid(surface, cells)
                        gameObj.draw_gen(font, surface, gen)
                        pygame.display.update()
                        continue
        
        if not paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                        continue
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        continue
                    
            cells, gen = gameObj.inc_gen(surface, cells, gen)
            gameObj.draw_grid(surface, cells)
            gameObj.draw_gen(font, surface, gen)
            pygame.display.update()
            clock.tick(game.FPS)
        
            
    #Exiting
    print("Exiting Application")
    pygame.quit()

#Main script
main()
