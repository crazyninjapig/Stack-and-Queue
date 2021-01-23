class Queue:
    def __init__(self):
        self.items = []

    #append new items into self.items list
    def Append(self, newItem):
        self.items.append(newItem)
    
    #creating a pop for the stack FIFO
    def Pop(self):
        lastItem = self.items[0]

        createList = []

        for i in range(1, len(self.items)):
            createList.append(self.items[i])


        self.items = createList

        return lastItem

    #checks if item is in the items list, returns true if there is that item in the list. if item is not in list return false
    def Contains(self, item):

        if item in self.items:
            return True
        else:
            return False