x = int(input("What's X? "))
y = int(input("What's Y? "))

if x < y:
    print("X is less than Y")
    
elif x > y:
    print("X is greater than Y")
    
elif x > y:
    print("X is equal than Y")
    

#else
if x < y:
    print("X is less than Y")
    
elif x > y:
    print("X is greater than Y")
    
else:
    print("X is equal than Y")
    
# or

if x>y or x<y:
    print("X is not equal to Y")
else:
     print("X is equal to Y")

#this can be optimized
if x!=y:
    print("X is not equal to Y")
else:
     print("X is equal to Y")

#