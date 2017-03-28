import numpy as np
import catch_errors


def linear_weighted_moving_average(data, period):
    """
    Linear Weighted Moving Average.
    LWMA = SUM(DATA[i]) * i / SUM(i)
    """
    catch_errors.check_for_period_error(data, period)

    idx_period = range(1, period+1)
    lwma = map(
        lambda idx:
        (sum([i * idx_period[data[idx-(period-1):idx+1].index(i)] for i in data[idx-(period-1):idx+1]])) / sum(range(1, len(data[idx+1-period:idx+1])+1)),
        range(period-1, len(data))
        )
    non_computable_values = np.repeat(np.nan, len(data) - len(lwma))
    lwma = np.append(non_computable_values, lwma)
    return lwma
