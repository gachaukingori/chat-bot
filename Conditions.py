x = int(input("Enter your Age: "))
if x<18:
    print("You are a minor")
elif x >18 and x <35:
    print("You are a Youth")
else:
    print("You are too old at age " +str(x))
    
