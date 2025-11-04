import numpy as np

from modules.utils import *


def top_k_discords(matrix_profile: dict, top_k: int = 3) -> dict:
    """
    Find the top-k discords based on matrix profile

    Parameters
    ---------
    matrix_profile: the matrix profile structure
    top_k: number of discords

    Returns
    --------
    discords: top-k discords (indices, distances to its nearest neighbor and the nearest neighbors indices)
    """
 
    discords_idx = []
    discords_dist = []
    discords_nn_idx = []

    # INSERT YOUR CODE

    mp_copy = matrix_profile['mp'].copy()
    profile_indices = matrix_profile['mpi']
    excl_zone = matrix_profile['excl_zone']

    for _ in range(top_k):
        # Находим индекс максимального значения
        max_idx = np.argmax(mp_copy)

        if np.isinf(mp_copy[max_idx]):
            break

        # Сохраняем индекс и расстояние
        discords_idx.append(max_idx)
        discords_dist.append(mp_copy[max_idx])

        # Сохраняем индекс ближайшего соседа
        discords_nn_idx.append(profile_indices[max_idx])

        # Применяем зону исключения, чтобы не найти соседей
        apply_exclusion_zone(mp_copy, max_idx, excl_zone, -np.inf) # Заменяем на -inf
    return {
        'indices' : discords_idx,
        'distances' : discords_dist,
        'nn_indices' : discords_nn_idx
        }
