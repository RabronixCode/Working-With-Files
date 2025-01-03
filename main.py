with open("file1.txt", "w") as file:
    file.write("HIII!")

with open("file1.txt", "r") as file:
    content = file.read()
    print(content)

with open("file1.txt", "a") as file:
    file.write("\nNEW LINE!")