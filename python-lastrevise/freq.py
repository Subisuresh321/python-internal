name=input("Enter you name: ")
name_list=set(name)
print(name_list)
for i in name_list:
    print(f"{name} contains {name.count(i)} {i}")

