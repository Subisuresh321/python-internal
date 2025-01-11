str1=input("Enter the String")
limit=int(input("Enter the limit"))
striped_str=str1.replace(" ","")

if(len(striped_str)%limit!=0):
    print(f"The string cannot be equally divided into {limit} rows")
else:
    substring_len=len(striped_str)//limit
    for i in range(0,len(striped_str),substring_len):
        print(striped_str[i:i+substring_len])