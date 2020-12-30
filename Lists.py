#Data Structures
#1 LISTS
mylist = ['V','I','C','T','O','R']
#a1 => mutable
mylist[2] = "J"
#chnages the item on index 2 to J
#print(mylist)
#append - Adds item at the end of list
mylist.append('G')
print(mylist)
#name = input("Enter The FNAME: ")

# Extend - appends all items from iterable eg list, string or tuple
#mylist.extend(name)
#print(mylist)
#insert - adds item at a given position
mylist.insert(2,'K')
print(mylist)

#Remove Value  (X) from the list
mylist.remove("K")
print(mylist)

#pop - removes item from given position
mylist.pop(3)
print(mylist)

#clear - removes all items

#COUNT - number of times an element appears on the list
print(mylist.count('4'))
#INDEX RETURNS INDEX OF THE FIRST ITEM WITH VALUE # XXX:
print(mylist.index('O'))


#USING LISTS AS STACK - LAST IN FIRST OUT (LIFO)
#ADDING - USE APPEND
mylist.append("H")
print(mylist)

#REMOVE USE POP
print(mylist.pop())


#USE LIST AS QUEUES, FIRST IN FIRST OUT FIFO
from collections import deque
myQ = deque(["Jennifer", "Flora", "Shelmith"])
myQ.append("Wangui")

print(myQ)
myQ.popleft()

print(myQ)
#CREATING LISTS

mylist.clear()
# CREATES A LIST WITH ALL THE SQUARES FROM 0 - 9
for x in range(10):
    mylist.append(x ** 2)
print(mylist)

#NESTED LISTS Eg MATRIX 3 * 4
matrix = [
[0,8,9,4],
[9,6,7,1],
[8,7,1,2],
]
#DEL VS POP
vowels = ['a','e','i','o','u']
vowels.pop(3)
print(vowels)
del vowels[3]
print(vowels)
print(len(vowels))
