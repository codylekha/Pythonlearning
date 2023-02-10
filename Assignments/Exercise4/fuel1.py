def main():
    f = get_fuel("Fraction: ")
    x,y = f.split("/")
    x = int(x)
    y = int(y)
    op = round((x/y),2)
    #print(op)
    if op >= 0.99: print("F")
    elif op <= 0.01: print("E")
    else: print(f"{op}")
    

def get_fuel(prompt):
    try:
         return input(prompt)
    except (ValueError,ZeroDivisionError):
        pass


main()