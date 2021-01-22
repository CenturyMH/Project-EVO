# import re, itertools

# with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r", encoding="utf-8") as file1:
#     with open(r"C:\Users\Martin\Desktop\python_test\testing2.txt", mode="w+", encoding="utf-8") as file2:
#         for line in file1:
#             id = re.search(r"([^\s]+)", line).group()
#             file2.write(id + "\n")

# # GENERATORS ARE DOPE, LEARN MORE
# # https://docs.python.org/dev/reference/expressions.html#generator-expressions
# # https://docs.python.org/3/library/itertools.html
# # Goal: do algorithm without using lists. Try writing one line at a time.
# # One line per loop iteration.
# # id gets new definition every loop, go from there


x = [1, 2, 3]
y = [4, 5, 6]


listcomp = [(a, b) for a in x for b in y]
newgen = ((a, b) for a in x for b in y)

