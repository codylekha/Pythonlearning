def convert(e):
    e=e.replace("):","🙂")
    e=e.replace(":(" , "🙁")
    return e

def main():
    emoji = input()
    output = convert(emoji)
    print(output)

main() 
'''
hello ):
hello 🙂

good bye :(
good bye 🙁


PS C:\Users\DELL\Python30days> hello ):
hello 🙂
PS C:\Users\DELL\Python30days> good bye :(
good bye 🙁
'''