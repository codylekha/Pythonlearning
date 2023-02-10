def main():
    string= input("Input: ")
    print("Output: ",end='')
    twtter(string)

def twtter(str):
    for s in str:
        ch = ''
        lst = ['a','e','i','o','u','A','E','I','O','U']
        if s not in lst:
            ch = ch + s
        for   c in ch :
            print(c, end='')


main()