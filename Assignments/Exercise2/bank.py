s = input("Greeting: ")
if s.startswith(('Hello','hello')):
    print("$0")
elif s.startswith(('H','h')):
    print("$20")
else:
    print("$100")


#str.startswith(prefix[, start[, end]])


#s = "hello"
#str = s.startswith(('H','h'))
#print(str)