import numpy as np

from modules.metrics import ED_distance, norm_ED_distance, DTW_distance
from modules.utils import z_normalize


class PairwiseDistance:
    """
    Distance matrix between time series 

    Parameters
    ----------
    metric: distance metric between two time series
            Options: {euclidean, dtw}
    is_normalize: normalize or not time series
    """

    def __init__(self, metric: str = 'euclidean', is_normalize: bool = False) -> None:

        self.metric: str = metric
        self.is_normalize: bool = is_normalize
    

    @property
    def distance_metric(self) -> str:
        """Return the distance metric

        Returns
        -------
            string with metric which is used to calculate distances between set of time series
        """

        norm_str = ""
        if (self.is_normalize):
            norm_str = "normalized "
        else:
            norm_str = "non-normalized "

        return norm_str + self.metric + " distance"


    def _choose_distance(self):
        """ Choose distance function for calculation of matrix
        
        Returns
        -------
        dict_func: function reference
        """

        dist_func = None

        if self.metric == 'euclidean':
            dist_func = ED_distance
        elif self.metric == 'dtw':
            # Можно использовать лямбда-функцию, чтобы передать параметр r, если он нужен
            dist_func = lambda ts1, ts2: DTW_distance(ts1, ts2, r=1.0)
        else:
            raise ValueError(f"Неизвестная метрика: {self.metric}. Доступные: 'euclidean', 'dtw'")

        return dist_func


    def calculate(self, input_data: np.ndarray) -> np.ndarray:
        """ Calculate distance matrix
        
        Parameters
        ----------
        input_data: time series set
        
        Returns
        -------
        matrix_values: distance matrix
        """
        
        num_series = input_data.shape[0]
        matrix_values = np.zeros(shape=(num_series, num_series))
        
        dist_func = self._choose_distance()
        
        # Создаем копию данных, чтобы не изменять исходный массив
        data = input_data.copy()

        # Нормализация данных, если флаг is_normalize установлен в True
        if self.is_normalize:
            for i in range(num_series):
                data[i] = z_normalize(data[i])

        # Вычисляем только верхний треугольник матрицы для оптимизации
        for i in range(num_series):
            for j in range(i + 1, num_series):
                # Вычисляем расстояние между i-м и j-м рядами
                distance = dist_func(data[i], data[j])
                
                # Заполняем матрицу симметрично
                matrix_values[i, j] = distance
                matrix_values[j, i] = distance

        return matrix_values
