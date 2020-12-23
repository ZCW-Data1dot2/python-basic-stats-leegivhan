from statszcw import zmean
from statszcw import zcount

def zvariance(list_in) -> float:
    """
    Finds variance of given list
    :param list: list of values
    :return: float
    """

    # Amanda
    var_top = 0
    data_mean = zmean(list_in)
    for val in list_in:
        diff = float(val) - data_mean
        sq_diff = diff ** 2
        var_top += sq_diff
    count_val = zcount(list_in) - 1
    var = var_top / count_val
    return float(var)

    # Derek
    # n = zcount(list)
    # mean = zmean(list)
    # d = [(x - mean) ** 2 for x in list]
    # v = sum(d) / (n - 1)
    # return round(v, 5)

    # Anusha
    # mean = zmean(list)
    # return sum((x - mean) ** 2 for x in list) / zcount(list)

print(zvariance([3, 5, 2, 10, 1, 3]))
