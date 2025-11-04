import numpy as np

from modules.utils import *


def top_k_motifs(matrix_profile: dict, top_k: int = 3) -> dict:
    """
    Find the top-k motifs based on matrix profile

    Parameters
    ---------
    matrix_profile: the matrix profile structure
    top_k : number of motifs

    Returns
    --------
    motifs: top-k motifs (left and right indices and distances)
    """

    motifs_idx = []
    motifs_dist = []

    # INSERT YOUR CODE

    # Создаем копию матричного профиля, чтобы не изменять исходный
    mp_copy = matrix_profile['mp'].copy()
    
    # Получаем необходимые данные из словаря
    profile_indices = matrix_profile['mpi']
    excl_zone = matrix_profile['excl_zone']

    # Ищем k мотивов
    for _ in range(top_k):
        # Находим индекс минимального значения в текущем матричном профиле
        min_idx = np.argmin(mp_copy)
        
        # Если минимальное значение - бесконечность, значит, мы нашли все возможные мотивы
        if np.isinf(mp_copy[min_idx]):
            break
            
        # Сохраняем расстояние
        motifs_dist.append(mp_copy[min_idx])
        
        # Находим индекс соответствующего ему мотива
        match_idx = profile_indices[min_idx]
        
        # Сохраняем пару индексов, отсортировав их для удобства
        motifs_idx.append(tuple(sorted((min_idx, match_idx))))

        # Применяем зону исключения к обоим найденным мотивам в копии
        # матричного профиля, чтобы не найти их снова
        apply_exclusion_zone(mp_copy, min_idx, excl_zone, np.inf)
        apply_exclusion_zone(mp_copy, match_idx, excl_zone, np.inf)

    return {
        "indices" : motifs_idx,
        "distances" : motifs_dist
        }
