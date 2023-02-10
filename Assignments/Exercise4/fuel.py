def get_fuel(fraction): 
    while True:
        try:
            x,y = fraction.split("/")
            op = (int(x)/int(y))
            return op
            

        except ValueError:
            pass
        except ZeroDivisionError:
            break

            

def main():
    fraction = input("Fraction: ")
    op = get_fuel(fraction)
    op = int(op)
    if op > 0.99: print("F")
    elif op < 0.01: print("E")
    else: print(f"{op}")
    
   
 
main()