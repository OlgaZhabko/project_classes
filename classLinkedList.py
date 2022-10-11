#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class ObjList:
    '''represents an object in a linked list'''
    def __init__(self, data):
        self.__data = data
        self.__next = self.__prev = None
    
    def set_next(self, obj):
        self.__next = obj
    
    def get_next(self):
        return self.__next
    
    def set_prev(self, obj):
        self.__prev = obj
    
    def get_prev(self):
        return self.__prev
    
    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data


class LinkedList:
    '''represents class which controlls a linked list'''
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj
    
    def remove_obj(self):
        if self.tail is None:
            return
        temp = self.tail.get_prev()
        if temp:
            temp.set_next = None
        self.tail = temp
        if self.tail is None: self.head = None
    
    def get_data(self):
        data_list = []
        first = self.head
        while first:
            data_list.append(first.get_data())
            first = first.get_next()
        return data_list
