import re

# def readwrite(id):
#     with open(r"C:\Users\Martin\Desktop\python_test\textfiletest.txt", mode="r") as f:
#         for line in f:
#             # if id in line:
#             # numtest = re.search("\d", line)
#             # if numtest.group()
#             print(line)

# readwrite()
# test = ["abc1", "def2", "ghi3"]
test = ["abc1", "def2", "ghi3", ]
result = []
for i in range(len(test)):
    if int(re.search(r"\d", test[i]).group()) > 1:
        result.append(test[i])

print(result)

# non commented code shows how to extract only the strings i want based on regex matches