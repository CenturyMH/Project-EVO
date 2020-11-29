import re

lines_to_write = []
def rewrite():
    with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as f:
        for position1, iter1 in enumerate(f):
            taxonID1 = re.match(r"[^\s]+", iter1).group()
            for position2, iter2 in enumerate(f):
                taxonID2 = re.match(r"[^\s]+", iter2).group()
                if taxonID1 in iter2:
                    if position1 == position2:
                        lines_to_write.append(iter1)
                    # else:
#                         print(position1, position2)

rewrite()
# print(lines_to_write)

# TRY: seek() counts every character in file, so use length of line to find position
# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes
# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write
