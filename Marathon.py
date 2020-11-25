import re

lines_to_write = []
def rewrite():
    with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as f:
        lines = f.read().splitlines()
        # print(lines)
        print(f.readlines())
        for iter1 in lines:
            taxonID = re.match(r"[^\s]+", iter1).group()
            for iter2 in lines:
                if taxonID in iter2 and taxonID != re.match(r"[^\s]+", iter2).group():
                    lines_to_write.append(iter2)

rewrite()
print(lines_to_write)

# Try: in first loop, store position of line of taxonID and use that to exclude lines with
# taxonID that are not in the same position?
# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes
# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write
