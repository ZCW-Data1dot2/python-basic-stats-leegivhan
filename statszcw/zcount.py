def zcount(list) -> float:
    """
    returns the number of elements in a list
    :param list: list of elements
    :return: int representing number of elements in given list
    """
    c = 0
    for _ in list:
        c += 1
    return c

if __name__ == "__main__":
    print(zcount([1,2,3,4]))
# - zmode(list: List[]) -> float
# - zmedian(list: List[]) -> float
# - zvariance(list: List[]) -> float
# - zstddev(list: List[]) -> float
# - zstderr(list: List[]) -> float
# - zcorr(listx: List[], listy: List[]) -> float