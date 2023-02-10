def einstein(m):
    c = 300000000
    E = m * pow(c,2)
    return E

def main():
    mass = int(input("m: "))
    E = einstein(mass)
    print("E:" , E)

main()


'''
m: 50
E: 4500000000000000000
'''