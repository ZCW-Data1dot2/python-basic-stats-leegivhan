def zvariance(list) -> float:
    # number of items in list
    n = len(list)
    # Mean of data
    mean = sum(list) / n
    # Square deviations
    deviations = [(i - mean) ** 2 for i in list]
    # Variance
    variance = sum(deviations) / n
    return variance

# print(zvariance([3, 5, 2, 7, 1, 3]))
