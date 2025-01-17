year=int(input("Enter the year"))
if(year%100==0):
    if(year%400==0):
        print(f"{year} is leap")
    else:
        print(f"{year } is not")
else:
    if(year%4==0):
        print(f"{year} is leap")
    else:
        print(f"{year } is not")