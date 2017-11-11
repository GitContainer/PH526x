import random, math

random.seed(1)


def in_circle(x, origin=[0] * 2):
    return x[0] - origin[0] < 1 and x[1] - origin[1] < 1


x = (1, 1)
print(in_circle(x, origin=(0, 0)))
