import re

def readwrite():
    with open(r"C:\Users\Martin\Desktop\python_test\textfiletest.txt", mode="r") as f:
        for line in f:
            # firstletter = "d"
            # if firstletter in line:
            # numtest = re.search("\d", line)
            # if numtest.group()
            print(line)

# readwrite()
test = "abc123"
numtest = re.search(r"\d+", test)

print(numtest.group(0))