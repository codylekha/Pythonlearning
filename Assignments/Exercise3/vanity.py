def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = ['1','2','3','4','5','6','7','8','9','0']
    if s.isupper() and (len(s)>=2 and len(s) <=6) :
        





main()