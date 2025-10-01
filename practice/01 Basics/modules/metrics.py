import numpy as np

from modules.utils import z_normalize

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

    # Получаем длину временных рядов
    n = len(ts1)
    
    # Применяем Z-нормировку к обоим временным рядам
    norm_ts1 = z_normalize(ts1)
    norm_ts2 = z_normalize(ts2)
    
    # Скалярное произведение нормализованных временных рядов
    dot_product = np.dot(norm_ts1, norm_ts2)
    
    # Среднее значение обоих нормализованных временных рядов (равно нулю после z-нормировки)
    mu_norm_ts1 = np.mean(norm_ts1)
    mu_norm_ts2 = np.mean(norm_ts2)
    
    # Стандартное отклонение нормализованных временных рядов (равно единице после z-нормировки)
    sigma_norm_ts1 = np.std(norm_ts1)
    sigma_norm_ts2 = np.std(norm_ts2)
    
    # Знаменатель
    denominator = n * sigma_norm_ts1 * sigma_norm_ts2
    
    # Расчёт нормализованной Евклидовой дистанции
    numerator = abs(2 * n * (1 - ((dot_product - n*mu_norm_ts1*mu_norm_ts2)/denominator)))
    norm_ed_dist = np.sqrt(np.abs(numerator))
    
    return norm_ed_dist


def DTW_distance(ts1: np.ndarray, ts2: np.ndarray, r: float = 1) -> float:   
    """    
    Calculate DTW distance

    Parameters
    ts1: first time series
    ts2: second time series
    r: warping window size (as a percentage of the time series length)

    Returns
    dtw_dist: DTW distance between ts1 and ts2
    """

    n = len(ts1)
    m = len(ts2)
    
    # Вычисляем размер окна поиска в абсолютных значениях
    r = int(np.ceil(n * r))

    # Создаем матрицу dtw размером (n+1) x (m+1) и инициализируем ее значениями бесконечности
    dtw_matrix = np.full((n + 1, m + 1), np.inf)
    # Инициализируем начальный элемент нулевым значением
    dtw_matrix[0, 0] = 0

    # Заполняем матрицу dtw, используя динамическое программирование
    for i in range(1, n + 1):
        # Определяем границы окна поиска
        start = max(1, i - r)
        end = min(m + 1, i + r + 1)
        for j in range(start, end):
            # Вычисляем евклидово расстояние между текущими элементами временных рядов
            cost = (ts1[i-1] - ts2[j-1])**2 
            # Вычисляем минимальную стоимость из соседних ячеек
            last_min = min(dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1])
            # Записываем общую стоимость в текущую ячейку
            dtw_matrix[i, j] = cost + last_min

    # DTW расстояние - это значение в правом нижнем углу матрицы
    dtw_dist = dtw_matrix[n, m]

    return dtw_dist
