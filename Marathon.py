import re

lines_to_write = []
# def rewrite():
with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as f:
    lines = f.readlines()
        # for position1, iter1 in enumerate(f):
        #     taxonID1 = re.match(r"[^\s]+", iter1).group()
        #     for position2, iter2 in enumerate(f):
        #         taxonID2 = re.match(r"[^\s]+", iter2).group()
        #         if taxonID1 in iter2:
        #             if position1 == position2:
        #                 lines_to_write.append(iter1)
                    # else:
#                         print(position1, position2)
for line in lines:
    print(line)

print("\n\n")
for line in lines:
    if "456" == re.match(r"[^\s]+", line).group():
        print(line)

# rewrite()
# print(lines_to_write)

# https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-file
# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes
# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write
