import re

def rewrite(id):
    with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as f:
        for line in f:
            print(line, end="")

        print("\n\n")
        f.seek(0)
        for line in f:
            first_item = re.match(r"[^\s]+", line).group()
            if id in line:
                if first_item == id:
                    print(line, end="")
                else:
                    pass

rewrite("123")

# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes
# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write
