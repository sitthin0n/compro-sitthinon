colum = int(input("Enter the number of colum: "))
for i in range(1,101):
    print(f"{1:3}", end=" ")
    if i % colum == 0:
        print()