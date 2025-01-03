import os
import time

# READ WRITE APPEND
with open("file1.txt", "w") as file:
    file.write("HIII!")

with open("file1.txt", "r") as file:
    content = file.read()
    print(content)

with open("file1.txt", "a") as file:
    file.write("\nNEW LINE!")

# BINARY FILE COPY
with open("image.png", "rb") as image:
    with open("image_copy.png", "wb") as copy:
        copy.write(image.read())

path = "C:\\Users\\User\\Desktop\\Python\\Working_With_Files\\file_scripts\\file1.txt"

size = os.path.getsize(path)
print(size)


print(os.path.getctime(path))
creation_time = time.ctime(os.path.getctime(path))
modification_time = time.ctime(os.path.getmtime(path))
print(creation_time, "AAAAAA", modification_time)