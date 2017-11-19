import numpy as np

from week3.casestudy3.k_nearest_predict import knn_predict


def make_prediction_grid():
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arrange(x_min, x_max, h)
    ys = np.arrange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k)

    return (xx, yy, prediction_grid)
