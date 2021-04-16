file = open("output.txt", "w")
file.write(input("Ecrire une phrase:"))

file = open("output.txt", "r")
print(file.read())

file.close()