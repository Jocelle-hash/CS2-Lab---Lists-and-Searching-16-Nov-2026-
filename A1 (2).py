
item = []

for i in range(4):
    items = input("enter school supplies: ")
    item.append(items)
for i in range(len(item)):
    print(i + 1, item[i])