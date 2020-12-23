def zmode(list) -> float:
    """Finds mode of given list
    :param list: list of values
    :return: int, float, None if no mode, or list if multiple modes"""
    # mode = 0
    # mode_count = 0
    for i in list:
        mode_count = 0
        mode = 0
        # index = 0
        for i in list:
            if list.count(i) > mode_count:
                mode_count = list.count(i)
                mode = i
        return mode

# print(zmode([1, 2, 3, 4, 2, 2, 3]))

            # mode_count += 1
            # index += 1


