file = input("File name: ")

if file.endswith('.gif'):
    print("images/gif")
 
elif file.endswith(('.jpg','jpeg')):
    print("images/jpeg")
 
elif file.endswith('.png'):
    print("images/png")
 
elif file.endswith('.pdf'):
    print("images/pdf")
 
elif file.endswith('.txt'):
    print("images/txt")
 
elif file.endswith('.zip'):
    print("images/zip")
 
else:
    print("application/octet-stream")