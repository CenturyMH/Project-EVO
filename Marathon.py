import re

id_list = []
with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as file1:
    lines_list = [line[:-1].split(" ") for line in file1]
    for line in lines_list:
        id_list.append(line[0])


with open(r"C:\Users\Martin\Desktop\python_test\testing2.txt", mode="w+") as file2:
    for i, id in enumerate(id_list):
        if any([id in line and id != line[0] for line in lines_list]):
            file2.write(str(lines_list[i]))

# logic in algorithm works, need to modify it (line doesn't get written to file in preferred format)
# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes
# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write