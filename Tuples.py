#TUPLES FEATURES similar To lists except
#IMMUTABLE (unlike list which are mutable)
#HETEROGENOUS (list are mostly homogenous)
#ACCESSED THROUGH UNPACKING (list accessed through iteration)
#EXAMPLE
import Functions
myList = Functions.fib(34)
myTuple = 'victor', 23, 65.3,'Thindigua',myList
print(myTuple)

#CAN BE NESTED
nTuple = 'victor',(53,63, 'Windsor')
print(nTuple)

#EMPTY TUPLE using ()brackets
emptyTuple = ()
print(len(emptyTuple)) #prints 0

#one item tuple - with a comma at the end
singleTuple = 'Myself',
print(len(singleTuple))  #prints 1
