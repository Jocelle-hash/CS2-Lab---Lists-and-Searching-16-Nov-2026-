
entry = input("Name (or done): ")
Names = []

while entry != "done":
    Names.append(entry)
    entry = input("Name (or done) ")

search = input("find a name: ") 
def find(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i + 1
    return -1

print(search, "is member number", find(Names, search))