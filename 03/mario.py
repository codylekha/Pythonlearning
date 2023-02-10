for _ in range(3):
    print("#")

# for abstraction concept & reusing same functions we creating func
def main():
    print_coln(3)

def print_coln(height):
    for i in range(height):
        print("#")
# OR USE PRINT("#" * HEIGHT)
main()

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
print("------------------------------")

def main():
    print_square(3)

def print_square(size):
    for i in range(size): #each row in a square
        for j in range(size): #each brick in row
            print("#", end='') #print brick
        print()
main()


