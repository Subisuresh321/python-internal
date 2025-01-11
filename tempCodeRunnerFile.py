with open('csv2.csv','a+') as csv2:
        writer=csv.DictWriter(csv2,fieldnames=['Name','Length'])
        writer.writeheader()
        writer.writerows(dict_list)
        