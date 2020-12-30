#Strings
print('This is A string')
#escape quotes
print("it doesn't matter")
# new line
print("The name willl be on the next line \n Gachau")
name = "The name willl be on the next line \n Gachau"
print(name)
#Concatenation
name = "Vic" "TOR"
print("Victor " "gachau")
print(2 * "v" + "ictor")
name = "victor"
print("the last letter of the name is " + name[-1])
print(name[0:-1])
#length of a String
print(len(name))
for i in range(len(name)):
    print(name[i])
#change character of  a String
print("P" + name[1:])
#LISTS

mylist = ["Cow", 4, 2.23, name]
print(mylist[-2])
print(mylist[1:])
mysecondlist = ["sheep", 43, 9339.0394, "Gachau"]
print(mylist+mysecondlist)
#lists are mutable
mylist[2] = 2**33
print(mylist)
a,b = 0,1
while a < 10:
     print(a)
     a, b = b, a+b
x = int(input("Kindly type anything: "))
if x==0:
    print(  " is a negative integer")
elif x == 5:
    print("corrext !")
else:
    print("wrong")
