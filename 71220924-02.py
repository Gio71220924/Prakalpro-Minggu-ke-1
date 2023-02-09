x = input("x = ")

if "/" not in x:
    x = int(x)

else:
    fraction = x.split("/")
    a = float(fraction[0])
    b = float(fraction[1])
    x = a/b
    f = 3*x**3 - 12*x**2 + 7/15*x - 22/7
    print("hasilnya adalah", f)