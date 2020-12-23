from statszcw import zstddev
from statszcw import zcount
import math

def zstderr(list: List[float]) -> float:
    """
    Calculates standard error of mean of given list
    :param list: list of values
    :return: float rounded to 5 decimal places
    """
    return zstddev(list) / math.sqrt(zcount(list))