import re

id_list = []
with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r", encoding="utf-8") as file1:
    lines_list = [line[:-1].split(" ") for line in file1]
    for line in lines_list:
        id_list.append(line[0])


with open(r"C:\Users\Martin\Desktop\python_test\testing2.txt", mode="w+", encoding="utf-8") as file2:
    for i, id in enumerate(id_list):
        if any([id in line and id != line[0] for line in lines_list]):
            file2.write(" ".join(lines_list[i]) + "\n")
            print(i)


# current version repeats lines (doesn't check for exclusivity vs other IDs, only strings outside of ID)
# Goal: rewrite algorithm without using a list