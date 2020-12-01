import re

id_list = []
# def rewrite():
with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as file1:
    lines = file1.readlines()
    for line in lines:
        id_list.append(re.match(r"[^\s]+", line).group())


with open(r"C:\Users\Martin\Desktop\python_test\testing2.txt", mode="w+") as file2:
    new_id_list = []
    for line in lines:
        if re.match(r"[^\s]+", line).group() not in file2:
            pass

# rewrite()
# print(lines_to_write)

# https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-file
# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes
# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write