def egyptian_fractions(a, b) -> list:
    ls = []
    if a == 1:
        ls.append(b)
        return ls
    while True:
        larggest_unit_fraction = b // a + 1
        a, b = a * larggest_unit_fraction - b, b * larggest_unit_fraction
        ls.append(larggest_unit_fraction)
        if a == 1:
            ls.append(b)
            break
    return ls


print(egyptian_fractions(5, 121))
print(egyptian_fractions(5, 13))
