# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 07:24:57 2018

@author: SHARON T ALEXANDER
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
    
    def reverse(self):
        prev = None
        cur = self.head
        while(cur is not None):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head = prev
        return self.head
    
    def detectLoop(self):
        slow = self.head
        fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                print('Found Loop')
                return
            
        
#main
myList = LinkedList()
myRev = LinkedList()
num = list(map(int,input().split()))

for i in num:
    myList.push(i)
    
#myList.show()
#myList.reverse()
#myRev.head = myList.show()
#myNew = myList
#myNew.show()
#myRev.show()
#choice = 1
#while(choice == 1):    
#    myList.pop()
#    myList.show()
#    choice = int(input())

myList.head.next.next.next = myList.head

myList.detectLoop()

            
        
