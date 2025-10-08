import numpy as np

from modules.utils import z_normalize
from modules.metrics import ED_distance, norm_ED_distance


def brute_force(ts: np.ndarray, query: np.ndarray, is_normalize: bool = True) -> np.ndarray:
    """
    Calculate the distance profile using the brute force algorithm

    Parameters
    ----------
    ts: time series
    query: query, shorter than time series
    is_normalize: normalize or not time series and query

    Returns
    -------
    dist_profile: distance profile between query and time series
    """

    n = len(ts)
    m = len(query)
    N = n-m+1

    dist_profile = np.zeros(shape=(N,))

    # Если требуется нормализация, нормализуем запрос один раз перед циклом.
    if is_normalize:
        norm_query = z_normalize(query)
    else:
        norm_query = query

    # Итерируемся по всем возможным подпоследовательностям временного ряда.
    for i in range(N):
        # Извлекаем подпоследовательность T(i,m)
        subsequence = ts[i:i+m]
        
        # Если требуется нормализация, нормализуем текущую подпоследовательность.
        if is_normalize:
            norm_subsequence = z_normalize(subsequence)
        else:
            norm_subsequence = subsequence
            
        # Вычисляем евклидово расстояние и сохраняем его в профиль расстояний.
        # Используем norm_query, который является либо нормализованным, либо исходным запросом.
        dist_profile[i] = ED_distance(norm_query, norm_subsequence)

    return dist_profile
