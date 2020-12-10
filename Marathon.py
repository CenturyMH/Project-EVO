import re


with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r", encoding="utf-8") as file1:
    with open(r"C:\Users\Martin\Desktop\python_test\testing2.txt", mode="w+", encoding="utf-8") as file2:
        for line in file1:
            id = re.search(r"([^\s]+)", line).group()

# Goal: rewrite algorithm without using a list
