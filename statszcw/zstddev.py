from statszcw import zvariance
import math

def zstddev(list) -> float:
    """
    Calculates standard deviation of given list
    :param list: list of values
    :return: float rounded to 5 decimal places
    """

    var = zvariance.zvariance(list)
    std_dev = math.sqrt(var)
    return std_dev

if __name__ == "__main__":
    print(zstddev([1, 2, 3, 4, 2, 2, 3]))