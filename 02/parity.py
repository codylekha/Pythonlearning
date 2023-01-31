def main():
    x =int(input("Enter the number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
main()        