import re

def readwrite():
    with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="w") as f:
        for line in f:
            # if int(re.search(r"\d", line).group()) > 2:
            print(line)
            # f.write(line)


readwrite()
# test = ["abc1", "def2", "ghi3"]
# test = ["abc1", "def2", "ghi3", ]
# result = []
# for i in range(len(test)):
#     if int(re.search(r"\d", test[i]).group()) > 1:
#         result.append(test[i])

# print(result)

# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write
