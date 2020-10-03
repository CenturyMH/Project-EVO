import re

id_list = []
def taxa_id(taxonID):
    with open(r"C:\Users\Martin\Desktop\Taxonomy\taxa.txt", mode = "r", encoding="utf-8") as f:
        # pattern = re.compile("^" + taxonID + "\\t")
        # for match in re.finditer(pattern, f.read()):
        #     id_list.append(match)

        for line in f:
            if taxonID in line:
                id_list.append(line)

        
def vernac_id(taxonID):
    with open(r"C:\Users\Martin\Desktop\Taxonomy\vernacular.txt", mode = "r", encoding="utf-8") as f:
        # for line in f:
        #     if taxonID in line:
        #         id_list.append(line)

        pattern = re.compile(taxonID)
        for match in re.finditer(pattern, f.read()):
            id_list.append(match)


# Killer Whale: 35489682
vernac_id("35489682")
for i in id_list:
    print(i, "\n")
# test = "123"
# x = re.compile("^" + test + "\\t")
# y = "123\tbc123\tbc"

# for match in re.finditer(x, y):
#     print("ye")


# # to run taxa_id here, taxa.txt cannot be open