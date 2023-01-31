print('hello, world')

name = input("What is your name? ")

print("Hello, ", name)  #insert a space for comma

print("hello" + name) #prints only argument
print("hello", name) #prints along with space

#format string  var name inside double but prints required result instead of hello name
print("hello name")
print(f"hello {name}")   

#To print double quots inside string
print('hello, "friend"')
print("hello, \"friend\"")


name1 ="                     david         "
name1 = name1.strip()
name1 = name1.capitalize()  #it capitalize only 1st letter of word
print(name1)

name2 = "sachin won india match"
name2 = name2.title()  # it capitalizes 1st letter of each word
print(name2)


first , last = name.split(" ")
print(f"firstname: {first}, lastname: {last}")
x = input("What's your num ")
y = input("What's your num ")

z = x + y
print(z)
'''What's your num 1
What's your num 2
12
here the number is not adding so we need to put int function'''

a = int(input("What's your num "))
b = int(input("What's your num "))

c = a + b
print(c)
'''What's your num 1
What's your num 2
3   NOW the output is added we need to convert to int'''

aa = float(input("What's your num "))
bb = float(input("What's your num "))

cc = aa + bb
print(cc)
print(f"{cc:,}") # to format numbers 1000-> 1,000 like that

p = 10/3
print(f"{p:.2f}")

p1 = 10.3333333
p1 = round(p1, 2)
print(p1)

#*******************************************************************************************************

def hello():
    print("hello MR/MRS")


name = input("enter name ")
hello()
print(name)


def firstname(to):
    print(f"hello {to}")

fname = input("enter name ")
firstname(fname)


def hello(to="world"):
    print("hello,", to)

hello()
lname = input("enter name")
hello(lname)