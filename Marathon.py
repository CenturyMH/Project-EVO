import re

lines_to_write = []
def rewrite():
    with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as f:
        lines = f.read().splitlines()
        print(lines)
        for position1, iter1 in enumerate(lines):
            taxonID1 = re.match(r"[^\s]+", iter1).group()
            for position2, iter2 in enumerate(lines):
                taxonID2 = re.match(r"[^\s]+", iter2).group()
                if taxonID1 in iter2 and position1 == position2:
                    lines_to_write.append(iter1)

rewrite()
print(lines_to_write)

# Try: in first loop, store position of line of taxonID and use that to exclude lines with
# taxonID that are not in the same position?
# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes
# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write
