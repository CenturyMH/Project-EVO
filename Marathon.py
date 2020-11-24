import re

lines_to_write = []
def rewrite():
    with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as f:
        lines = f.read().splitlines()
        # print(lines)
        print(f.readlines()
        for iter1 in lines:
            first1 = re.match(r"[^\s]+", iter1).group()
            for iter2 in lines:
                first2 = re.match(r"[^\s]+", iter2).group()
                if first1 in iter2 and first1 != first2:
                    lines_to_write.append(iter2)

rewrite()

# syntax error in for loop i dont understand
# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes
# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write
