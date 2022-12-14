#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''these two classes imitate the popular sapper game'''
from random import randint

class Cell:
    '''Represents a cell of the gamefield'''
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False
    
    @property
    def is_mine(self):
        return self.__is_mine
    @is_mine.setter
    def is_mine(self, val):
        if type(val) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = val
    
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, val):
        if not isinstance(val, int) or val < 0 or val > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = val    
    
    @property
    def is_open(self):
        return self.__is_open
    @is_open.setter
    def is_open(self, val):
        if type(val) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = val    
    
    def __bool__(self):
        return not self.__is_open


class GameField:
    '''Represents the gamefield consisting of cells, realizes SingleTon pattern'''
    game = None
    cells_around = ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1))
    
    def __new__(cls, *args, **kwargs):
        if cls.game is None:
            cls.game = super().__new__(cls)
        return cls.game
    
    def __del__(self):
        GameField.__instance = None
    
    def __init__(self, n, m, total_mines):
        self.__m = m
        self.__n = n
        self.__t_m = total_mines
        self.__field_cells = None
    
    @property
    def field(self):
        return self.__field_cells
    
    def init_field(self):
        '''initializes the gamefield, sets the given number of mines random and counts number of mines around for each cell which does not contain a mine'''
        
        self.__field_cells = tuple(tuple(Cell() for _ in range(self.__m)) for _ in range(self.__n))
        mines = 0
        while mines < self.__t_m:                                         #sets mines randomly in the field
            i, j = randint(0, self.__n - 1), randint(0, self.__m - 1)
            if self.__field_cells[i][j].is_mine is True:
                continue
            self.field[i][j].is_mine = True
            mines+=1
        
        for i in range(self.__n):                                          # counts number of mines around each cell if there is no mine in the cell
            for j in range(self.__m):
                if self.field[i][j].is_mine is False:
                    mines = 0
                    res = sum(self.field[i+n][j+m].is_mine for n, m in self.cells_around if self.valid_indexes(i+n, j+m))
                    self.field[i][j].number = res
                    
    def valid_indexes(self, x, y):
        '''checks if indexes are correct'''
        return 0<=x<self.__n and 0<=y<self.__m
    
    def open_cell(self, i, j):
        '''opens a cell'''
        try:  
            self.field[i][j].is_open = True
        except:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_field(self):
        '''outputs the game field setting X for a closed cell, number of mines or * for open cells'''
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].is_open == False:
                    print('X'.ljust(3), end = '')
                elif self.field[i][j].is_mine == False:
                    print(str(self.field[i][j].number).ljust(3), end='')
                else:
                    print('*'.ljust(3), end = '')
            print()
