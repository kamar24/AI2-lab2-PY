def is_triangle_numbers(slowo):
    wynik = 0
    for x in range(slowo.__len__()):
        wynik += ord(slowo[x]) - 64
    check = 0;
    i = 1
    while check <= wynik:
        check = (i * (i + 1)) / 2
        i += 1
        if check == wynik:
            break
    if check == wynik:
        return slowo + " is triangle word"
    else:
        return slowo + " is not triangle word"
print(is_triangle_numbers("SKY"))
print(is_triangle_numbers("YKaaS"))