from statszcw import zcount
from statszcw import zstddev
from statszcw import zmean

def zcorr(list: List[float], list2: List[float]) -> float:
    """
    Calculates the correlation between two lists of values
    :param list: list of values
    :param list2: list of values
    :return: float rounded to 2 decimal places
    """

    sum = 0
    for i in range(0, len(list)):
        sum += ((list[i] - zmean(list)) * (list2[i]-zmean(list2)))
    cov = sum / (zcount(list)-1)
    corr = cov / (zstddev(list) * zstddev(list2))
    return round(corr, 2)