from Stack import Stack
from Queue import Queue

#Calling Stack and Queue 
testStack = Stack()
testQueue = Queue()

#Using push function to create a new list of words
testStack.Push("Beenus")
testStack.Push("Weenus")
testStack.Push("Freenus")

#Using append function to create a new list of words
testQueue.Append("Rat")
testQueue.Append("Snack")
testQueue.Append("Borlap")

#Testing if the Pop funciton works, 
# Checking whats in the lest, 
# Checking if list contains item that was popped, 
# Checking if list contains item that was not popped, 
# Checking if list contains item that never existed within it
print('Stack Test')
print(testStack.Pop())
print(testStack.items)
print(testStack.Contains('Beenus'))
print(testStack.Contains('Freenus'))
print(testStack.Contains('Wack'))

print('')

#Testing if the Pop funciton works, 
# Checking whats in the lest, 
# Checking if list contains item that was popped, 
# Checking if list contains item that was not popped, 
# Checking if list contains item that never existed within it
print('Queue Test')
print(testQueue.Pop())
print(testQueue.items)
print(testQueue.Contains('Snack'))
print(testQueue.Contains('Rat'))
print(testQueue.Contains('Wack'))