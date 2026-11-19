names = []
n = int(input("how many names? "))

for i in range(n):
    name = input("enter names: ")
    names.append(name)
    
print(names, end=" ")
print(n, "names stored")