file_string = ""
with open("referat.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        file_string += line
print(file_string)
print(len(file_string))
file_string = file_string.replace(".", "!")
print(len(file_string.split()))
print(file_string)

with open("referat2.txt", "w", encoding="utf-8") as my_file:
    my_file.write(file_string)
