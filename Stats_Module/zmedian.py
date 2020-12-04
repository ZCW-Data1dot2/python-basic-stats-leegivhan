def zmedian(list) -> float:
    list.sort()
    if len(list) % 2 != 0:
        return list[(int(len(list)/2))]
    elif len(list) % 2 == 0:
        return (list[(int(len(list)/2))] + list[(int(len(list)/2))-1]) / 2


# print(zmedian([1, 2, 3, 2, 2, 3]))
# print(zmedian([1, 6, 2, 3, 7, 2, 2, 3]))
# listo = [1, 2, 3, 2, 2, 3]
#
# print((listo[(int(len(listo)/2))] + listo[(int(len(listo)/2))-1])/2)
