import random
import time

start_time = time.clock()
ys = []
for rep in range(1000000):
    y = 0
    for k in range(10):
        x = random.choice(range(1, 7))
        y += x
    ys.append(y)
# plt.hist(ys);
end_time = time.clock()
print(end_time - start_time)
