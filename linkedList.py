# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 07:24:57 2018

@author: SHARON T ALEXANDER
new change
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def pop(self):
        if(self.head != None):
            self.head = self.head.next
        else:
            print('No More Elements!')
    
    def show(self):
        temp = self.head
        print(end = '\n')
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next

#main
myList = LinkedList()
num = list(map(int,input().split()))

for i in num:
    myList.push(i)
    
myList.show()
choice = 1
while(choice == 1):    
    myList.pop()
    myList.show()
    choice = int(input())



            
        
