lists = ['tom','Jack','luCy','lily','jErry','anna']
dics = {'jack':'python','Lucy':'jaVa','jeRry':'rUby','lily':'c#',}
new_lists = []
for i in lists:
    new_lists.append(i.lower())
print(new_lists)
new_dics = {}
for i,j in dics.items():
    new_dics[i.lower()] = j.lower()
print(new_dics)