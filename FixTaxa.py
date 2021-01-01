import re

id_list = []
with open(r"C:\Users\Martin\Desktop\python_test\testing1.txt", mode="r", encoding="utf-8") as file1:
    lines_list = [line[:-1].split(" ") for line in file1]
    for line in lines_list:
        if line[0] not in id_list:
            id_list.append(line[0])

with open(r"C:\Users\Martin\Desktop\python_test\testing2.txt", mode="w+", encoding="utf-8") as file2:
    for i, id in enumerate(id_list):
        # Problem is most likely right here. Conditional logic probably needs more complexity.
        if any([id in line and id != line[0] for line in lines_list]):
            pass
        else:
            file2.write(" ".join(lines_list[i]) + "\n")
            print(i)

print(id_list, "\n", lines_list, sep="")
# Killer Whale: 35489682
# Next goal: Make every taxonID unique in the file to the species (Get rid of subspecies)
# 3865179 lines were counted by looping through taxa.txt, took about 8-9 minutes