import re

# int(re.match(r"\d", line).group(0))
xd = []
def readwrite():
    with open(r"C:\Users\Martin\Desktop\Taxonomy\taxa.txt", mode="r") as f:
        for i, line in enumerate(f):
            white = re.match(r"([^\s]+)", line)
            if i == 3:
                break
            if white:
                print(line, white.group(), "yerr", "\n")
            else:
                print(line, "nope", "\n")

readwrite()
# print(readwrite(7))
# test = ["abc1", "def2", "ghi3"]
# test = ["abc1", "def2", "ghi3", ]
# result = []
# for i in range(len(test)):
#     if int(re.search(r"\d", test[i]).group()) > 1:
#         result.append(test[i])

# print(result)

# https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328#11469328
# try writing to new file instead of rewriting existing file, open first one in read and second in write
