from statszcw import zvariance
import math

def zstddev(list: List[float]) -> float:
    """
    Calculates standard deviation of given list
    :param list: list of values
    :return: float rounded to 5 decimal places
    """

    var = zvariance(list)
    std_dev = math.sqrt(var)
    return std_dev
