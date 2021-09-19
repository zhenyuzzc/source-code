squares=list(range(1,1000001)) 
print(min(squares))
print(max(squares))
print(sum(squares))
print()

js=list(range(1,21,2))
for valve in js:
    print(valve)
print()

bs=list(range(3,31,3))
for valve in bs:
    print(valve)
print()

lb=list(range(1,11))
print(lb)
for valve in lb:
    print(valve**3)
print()

lf=[valve**3 for valve in range(1,11)]
print(lf)
for valve in lf:
    print(valve)
