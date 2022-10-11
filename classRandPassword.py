#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from random import choice, randint
class RandomPassword:
    '''class to generate a random password of permitted symbols having length between min_length and max_length'''
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
    
    def __call__(self):
        return ''.join([choice(self.psw_chars) for _ in range(randint(self.min_length, self.max_length))])
        
min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
password_generator = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [password_generator() for _ in range(3)]

print('END')