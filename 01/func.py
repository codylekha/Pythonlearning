'''
name = input("enter input")
hello(name)


def hello(to):
    print("Hello ", to)

error hello is not defined
'''

'''
def hello(to):
    print("Hello ", to)

def main():
    name = input("enter input")
    hello(name)

main() #without calling this willnot execute anything

# Method 2*******************************************
def main():
    name = input("enter input")
    hello(name)

def hello(to):
    print("Hello ", to)

main()

#Method 3******************************

def hello(to):
    print("Hello ", to)

name = input("enter name")
hello(name)
#*****************************************


def hello(to="world"):
    print("hello,", to)

hello()   #hello world
name = input("enter name ")
hello(name) #hello david

c:/Users/DELL/Python30days/01/func.py> 
hello, world
enter name david
hello, david


#Return

def square(n):
    return n*n

x = int(input("ENTER THE NUM "))
print("x squared is ",square(x))

#but to calc more powers
'''
def main():
    x = int(input("Enter the num " ))
    print("x squared is ",square(x))

def square(n):
    return pow(n,3)
main()