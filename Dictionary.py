#uses Key:value pair with tthe key being unique in each dictionary eg associative array/memory

dictSet = {'name' : "Victor", 'age' : 23}
print(dictSet['age'])
dictSet['lname'] = "Gachau"
print(dictSet)
print(dictSet['lname'])

 #The dict() constructor builds dictionaries directly from sequences of key-value pairs:
print(dict([('name','gachau'),('age',23),('middlename','kingori')]))
import builtins
print(dir(builtins))
