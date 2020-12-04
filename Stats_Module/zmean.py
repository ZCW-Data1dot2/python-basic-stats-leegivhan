def zmean(list: list) -> float:
    """
    Gets mean of a numbers
    :param list:
    :return: mean of numbers
    """
    mean_list = 0
    for i in list:
        mean_list += i
    mean = mean_list / len(list)
    return mean

print(zmean([1, 2, 3, 4, 2, 2, 3]))