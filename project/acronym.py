user_input =str(input("enter the string"))
user_input = user_input.split()
print(user_input)
a = ''
for i in user_input:
    a = a + i[0].upper()
print(a)