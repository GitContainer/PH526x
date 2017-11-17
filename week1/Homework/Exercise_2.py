import random, math

random.seed(1)


def in_circle(x, origin=[0] * 2):
    return x[0] - origin[0] < 1 and x[1] - origin[1] < 1


R = 10000
x = []
inside = []
for i in range(R):
    point = [random.uniform(-2,2), random.uniform(-2,2)]
    x.append(point)
    if in_circle(point, origin=(0, 0)):
        inside.append(True)
    else:
        inside.append(False)

proportion = 0

for test in inside:
    if test:
        proportion += 1

print(proportion / R)
