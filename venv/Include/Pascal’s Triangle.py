def generate_pascal_row(s):
    len = s.__len__()
    wynik=[]
    for x in range(len + 1):
        if x == 0 or x == len:
            wynik.append(1)
        else:
            wynik.append(s[x - 1] + s[x])
    return wynik

print(generate_pascal_row([]))
print(generate_pascal_row([1, 2, 1]))
print(generate_pascal_row([1, 4, 6, 4, 1]))