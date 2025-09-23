import numpy as np


def ED_distance(ts1: np.ndarray, ts2: np.ndarray) -> float:
    """
    Calculate the Euclidean distance

    Parameters
    ----------
    ts1: the first time series
    ts2: the second time series

    Returns
    -------
    ed_dist: euclidean distance between ts1 and ts2
    """
    
    ed_dist = 0

    # INSERT YOUR CODE
        
    # Вычисляем сумму квадратов разностей элементов
    squared_diffs = np.sum((ts1 - ts2)**2)
    
    # Извлекаем квадратный корень из суммы
    ed_dist = np.sqrt(squared_diffs)
    return ed_dist


def norm_ED_distance(ts1: np.ndarray, ts2: np.ndarray) -> float:
    """
    Calculate the normalized Euclidean distance

    Parameters
    ----------
    ts1: the first time series
    ts2: the second time series

    Returns
    -------
    norm_ed_dist: normalized Euclidean distance between ts1 and ts2s
    """

    norm_ed_dist = 0

    # INSERT YOUR CODE

    return norm_ed_dist


def DTW_distance(ts1: np.ndarray, ts2: np.ndarray, r: float = 1) -> float:
    """
    Calculate DTW distance

    Parameters
    ----------
    ts1: first time series
    ts2: second time series
    r: warping window size
    
    Returns
    -------
    dtw_dist: DTW distance between ts1 and ts2
    """

    dtw_dist = 0

    # INSERT YOUR CODE
    m, n = len(ts1), len(ts2)
    
    # Матрица накопления расстояний
    D = np.zeros((m + 1, n + 1)) + np.inf
    D[0][0] = 0
    
    # Если окно не задано, применяем полное заполнение матрицы
    if r is None or r >= max(m, n):
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = (ts1[i - 1] - ts2[j - 1]) ** 2
                D[i][j] = cost + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
    else:
        # Ограничиваем окно размерами (+/- r вокруг диагонали)
        for i in range(1, m + 1):
            lower_bound = max(1, i - r)
            upper_bound = min(n, i + r)
            
            for j in range(lower_bound, upper_bound + 1):
                cost = (ts1[i - 1] - ts2[j - 1]) ** 2
                D[i][j] = cost + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
                
    return D[m][n]
    #return dtw_dist
