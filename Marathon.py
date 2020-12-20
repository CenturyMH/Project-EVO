# import re


# with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r", encoding="utf-8") as file1:
#     with open(r"C:\Users\Martin\Desktop\python_test\testing2.txt", mode="w+", encoding="utf-8") as file2:
#         for line in file1:
#             id = re.search(r"([^\s]+)", line).group()

# # FixTaxa was modified. Do more testing, and figure out why it doesn't work on taxa.txt

x = ["a", "b", "c"]

for i, id in x:
    print(i)
    print(id)

# https://stackoverflow.com/questions/42259166/python-3-valueerror-not-enough-values-to-unpack-expected-3-got-2
