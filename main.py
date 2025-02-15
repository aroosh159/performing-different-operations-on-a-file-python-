# open a file in read mode
file1 = open("profile.txt")

# read the file content
read_content = file1.read()
print(read_content)

# open the file2.txt in write mode
file2 = open('profile.txt', 'w')

# write contents to the file2.txt file
file2.write('Programming is Fun.\n')
file2.write('Programiz for beginners\n')

# open a file
file1 = open("profile.txt", "r")

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()

with open("profile.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)