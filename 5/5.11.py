lb = list(range(1,10))
i = 'th'
print(lb)
for valve in lb:
    if valve == 1:
        print("1st")
    elif valve == 2:
        print("2nd")
    elif valve == 3:
        print("3rd")
    else:
        print(f"{valve}{i}")
        