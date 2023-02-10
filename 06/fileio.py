print("1")


name = input("whats your name? ")

file=open("namew.txt", "w")
file.write(name)
file.close()




file=open("namea.txt", "a")
file.write(f"{name}\n")
file.close()



with open("names.txt", "w") as file:
    file.write(f"{name}\n")
