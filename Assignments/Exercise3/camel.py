def myfunc(case):
    for c in case:
        if c.isupper():
            r = c.replace(c, c.lower())
            r = '_' + r
            return r
        else:
            return case


def main():
    camelcase = input("camelCase: ")
    if True:
        print("snake_case:", camelcase)
    else:
        print("snake_case:", camelcase)

main()