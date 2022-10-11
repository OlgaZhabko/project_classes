#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from random import randint

class TickTackToe:
    '''Class to represent a classical popular game of noughts and crosses'''
    FREE_CELL = 0 
    HUMAN_X = 1  
    COMPUTER_O = 2
    
    def __init__(self):
        '''initializes the game'''
        self.__human_wins = False
        self.__computer_wins = False
        self.__draw = False
        self.field = tuple(tuple(Cell() for _ in range(3)) for k in range(3))
    
    @property
    def human_wins(self):
        return self.__human_wins
    
    @property
    def computer_wins(self):
        return self.__computer_wins
    
    @property
    def draw(self):
        return self.__draw
    
    def clear(self):
        '''clears the game field setting all cell values to 0'''
        for row in self.field:
            for cell in row:
                cell.value = 0
        self.computer_wins = self.human_wins = self.draw = False
    
    def __bool__(self):
        '''return True if there is no winner and not all cells are open'''
        return not self.computer_wins and not self.human_wins and not self.draw and any(bool(self.field[i][j]) for i in range(3) for j in range(3))
    
    def __getitem__(self, indxs):
        '''returns value of the cell in the field at given indexes'''
        if self.valid_indexes(indxs):
            i, j = indxs
        return self.field[i][j].value       
    
    def __setitem__(self, indxs, val):
        '''sets a new value into the cell if indexes are correct, value is correct and the cell is not open'''
        if self.valid_indexes(indxs):
            i, j = indxs
        if not self.field[i][j]:
            print(f'Клетка с индексами {i, j} уже занята, выберите другую клетку: ')
            return False
        self.field[i][j].value = val
        w = self.is_there_a_winner()
        if w == 1 : self.__human_wins = True
        if w == 2 : self.__computer_wins = True
        if not any(bool(self.field[i][j]) for i in range(3) for j in range(3)) and not self.__computer_wins and not self.__human_wins:
            self.__draw = True        
        return True

    @staticmethod
    def valid_indexes(args):
        '''Checks if the given indexes are correct (whole numbers 0-2) and returns True if so and raises IndexError otherwise'''
        if type(args)!=tuple or len(args)!=2 or any(not (0 <= ind < 3) for ind in args):
            raise IndexError('некорректно указанные индексы')
        return True
    
    def is_there_a_winner(self):
        '''checks if any column, row or diagonal contains all ones or all zeros 
        and return 1 if the human wins and 2 if the computer wins or None otherwise'''
        winner = 0
        for i in range(3):
            winner = set(self.field[i][j].value for j in range(3))
            if len(winner) == 1 and 0 not in winner:
                winner = winner.pop()
                return winner
    
        for j in range(3):
            winner = set(self.field[i][j].value for i in range(3))
            if len(winner) == 1 and 0 not in winner:
                winner = winner.pop()
                return winner

        winner = set(self.field[i][i].value for i in range(3))
        if len(winner) == 1 and 0 not in winner:
            winner = winner.pop()
            return winner

        winner = set(self.field[i][2-i].value for i in range(3))
        if len(winner) == 1 and 0 not in winner:
            winner = winner.pop()
            return winner    
            
    
    def human_go(self):
        '''sets a cross into a free cell by indexes given by the human, if the indexes are not correct or the cell is not free asks to enter indexes again'''
        print('Укажите через пробел индексы клетки, в которую Вы хотите поставить крестик "Х" (i и j, числа от 0 до 2): ')
        while True:
            try:
                i = j = None
                i, j = tuple(map(int, input().split()))
                res = self.__setitem__((i, j), self.HUMAN_X)
                if res:
                    break
                else:
                    continue
            except:
                print(f'Неверные индексы клетки, индексы должны быть числами 0, 1 или 2. Попробуйте ещё раз: ')
                continue            
        
    def computer_go(self):
        '''puts a nought into a random free cell'''
        print('Ход компьютера')
        while True:
            i, j = randint(0, 2), randint(0, 2)
            if self.field[i][j]:
                self.__setitem__((i, j), self.COMPUTER_O)
                break
    
    def show(self):
        '''Outputs the game field using X, O or # for free cells'''
        for row in self.field:
            print(*map(lambda x: 'X'.ljust(3) if x.value == 1 else 'O'.ljust(3) if x.value == 2 else '#'.ljust(3), row))

class Cell:
    '''This class decribes cells of the TickTackToe field and has one attribute: value (0 - the cell is free, 1 - there is a cross in the cell, 2 - there is a nought in the cell)'''
    def __init__(self):
        self.value = 0
        
    def __bool__(self):
        return self.value == 0


game = TickTackToe()
step_game = 0

while game:
    game.show()
    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
    step_game += 1

game.show()

if game.human_wins:
    print("Поздравляем! Вы победили!")
elif game.computer_wins:
    print("Компьюте выиграл, к сожалению. Но поробуйте ещё раз! Все получится, со временем!")
else:
    print("Ничья.")
