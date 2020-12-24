from statszcw import zcount
from statszcw import zstddev
from statszcw import zmean

def zcorr(list, list2) -> float:
    """
    Calculates the correlation between two lists of values
    :param list: list of values
    :param list2: list of values
    :return: float rounded to 2 decimal places
    """

    sum = 0
    for i in range(0, zcount.zcount(list)):
        sum += ((list[i] - zmean.zmean(list)) * (list2[i]-zmean.zmean(list2)))
    cov = sum / (zcount.zcount(list)-1)
    corr = cov / (zstddev.zstddev(list) * zstddev.zstddev(list2))
    return round(corr, 2)

if __name__ == "__main__":
    print(zcorr([1, 2, 3, 2, 2, 3],[1, 1, 3, 2, 1, 3]))