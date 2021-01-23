class Stack:

    def __init__(self):
        self.items = []


    def Push(self, newItem):
        #create list
        createList = []
        #append new items to list
        createList.append(newItem)
        
        for i in self.items:
            createList.append(i)
        #self.items is now the new list
        self.items = createList
    
    #creating a pop for the stack LIFO
    def Pop(self):

        firstItem = self.items[0]
  
        createList = []

        for i in range(1, len(self.items)):
            createList.append(self.items[i])

        self.items = createList

        return firstItem

    #checks if item is in the items list, returns true if there is that item in the list. if item is not in list return false
    def Contains(self, item):
        if item in self.items:
            return True
        else:
            return False