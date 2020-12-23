from statszcw import zcount

def zmean(list) -> float:
    """
    Returns mean of given list
    :param list: list
    :return: float
    """
    mean = sum(list) / zcount(list)
    return float(mean)
    # mean_list = 0
    # for i in list:
    #     mean_list += i
    # mean = mean_list / zcount(list)
    # return mean

print(zmean([1, 2, 3, 4, 2, 2, 3]))