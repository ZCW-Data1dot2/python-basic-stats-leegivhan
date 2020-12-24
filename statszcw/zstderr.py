from statszcw import zstddev
from statszcw import zcount
import math

def zstderr(list) -> float:
    """
    Calculates standard error of mean of given list
    :param list: list of values
    :return: float rounded to 5 decimal places
    """
    return zstddev.zstddev(list) / math.sqrt(zcount.zcount(list))

if __name__ == "__main__":
    print(zstderr([3, 5, 2, 10, 1, 3]))