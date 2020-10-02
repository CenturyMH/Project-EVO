id_list = []
def taxa_id(taxonID):
    with open(r"C:\Users\Martin\Desktop\Taxonomy\taxa.txt", mode = "r", encoding="utf-8") as f:
        for line in f:
            if str(taxonID) in line:
                id_list.append(line)

def vernac_id(taxonID):
    with open(r"C:\Users\Martin\Desktop\Taxonomy\vernacular.txt", mode = "r", encoding="utf-8") as f:
        for line in f:
            if str(taxonID) in line:
                id_list.append(line)

taxa_id("Orcinus orca")
for i in id_list:
    print(i.splitlines())


# to run taxa_id here, taxa.txt cannot be open