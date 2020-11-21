import re

# int(re.match(r"\d", line).group(0))
xd = []
with open(r"C:\Users\Martin\Desktop\Taxonomy\taxa.txt", mode="r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            print(i)
        print("done")
# def readwrite(id):
#     with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r") as f:
        
#         for line in f:
#             white = re.match(r"[^\s]+", line)
#             if id in line:
#                 if white.group() == id:
#                     print(line)
#                 else:
#                     print(line, "delete this???")

# readwrite("123")
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
