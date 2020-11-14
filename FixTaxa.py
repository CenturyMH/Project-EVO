import re

id_list = []
def taxa_id(taxonID):
    with open(r"C:\Users\Martin\Desktop\Taxonomy\taxa.txt", mode="r", encoding="utf-8") as f:
        # my_pattern = re.compile(taxonID)
        # for match in re.finditer(my_pattern, f.read()):
        #     id_list.append(match.group(0))

        for line in f:
            if taxonID in line:
                firstWord = re.search(r"[^\s]+", line)
                if firstWord.group(0) == taxonID:
                    id_list.append(line)

def vernac_id(taxonID):
    with open(r"C:\Users\Martin\Desktop\Taxonomy\vernacular.txt", mode = "r", encoding="utf-8") as f:
        for line in f:
            if taxonID in line:
                id_list.append(line)

        # my_pattern = re.compile(taxonID)
        # for match in re.finditer(my_pattern, f.read()):
        #     id_list.append(match)


# Killer Whale: 35489682
taxa_id("35489682")
for i in id_list:
    print(i, "\n")

# Next goal: Make every taxonID unique in the file to the species (Get rid of subspecies)
# to run taxa_id here, taxa.txt cannot be open
