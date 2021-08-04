#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: Alice 'Ava' Williams
Date: July 29, 2021
File: game.py
Desc: Game class with associated methods and constants.
"""

import state
import numpy as np
import pygame

#Constants
TITLE = "John Conway's Game of Life GUI App"
FPS = 60
    
DIM = 20
WIDTH = 1280
HEIGHT = 960
    
#Colors
WHITE = (255, 255, 255) #State.DEAD
BLACK = (0, 0, 0)       #State.ALIVE
GREY = (128, 128, 128)  #Grid lines

ALIVE = state.State.ALIVE
DEAD = state.State.DEAD

class Game:
    
    def __init__(self): #Should move cells/generation count to instance variables.
        pass#
        
    
    #Functions
    
    
    def init_cells(self, dim_x, dim_y):
        cells = np.zeros((dim_y, dim_x), dtype = state.State)
    
        #Test oscillator
        cells[2, 2] = ALIVE
        cells[2, 3] = ALIVE
        cells[2, 4] = ALIVE
        
        #Test glider -- Collapses into a static block shape without wrapping.
        cells[6, 4] = ALIVE
        cells[7, 5] = ALIVE
        cells[7, 6] = ALIVE
        cells[6, 6] = ALIVE
        cells[5, 6] = ALIVE
        
        return cells
    
    
    def inc_gen(self, surface, grid, gen):
        new_grid = np.copy(grid)
        
        for row, col in np.ndindex(grid.shape):
            
            #Future Thoughts: How to abstract a ruleset inorder to allow for multiple rulesets?
            #num_alive calculation assumes out of bounds cells die, a toroidal wrap would be ideal.
            num_alive = np.sum(grid[row - 1 : row + 2, col - 1 : col + 2]) - grid[row, col]
            if grid[row, col] == ALIVE and (num_alive < 2) or (num_alive > 3): #Dead Conditional
                    new_grid[row, col] = DEAD
            elif num_alive == 3: #Alive Conditionaldim[0]
                    new_grid[row, col] = ALIVE
        
        gen += 1
        return new_grid, gen

    
    def draw_grid(self, surface, grid):
        surface.fill(GREY)
        for row, col in np.ndindex(grid.shape):
            color = BLACK if grid[row, col] == ALIVE else WHITE
            pygame.draw.rect(surface, color, (col*DIM, row*DIM, DIM-1, DIM-1))
    
    
    def draw_gen(self, font, surface, gen):
        text = font.render('Gen: ' + str(gen), True, (0, 0, 255))
        surface.blit(text, (WIDTH - 180, 14))
        pass


    def save_grid(self, grid): #Does not account for generation change.
        print("Saving state to file...")
        np.save("save_file.npy", grid)
        
    
    def load_grid(self): #Does not account for generation change.
        print("Loading state from file...")
        return np.load("save_file.npy", allow_pickle=True)
