
import random
import matplotlib.pyplot as plt
import numpy as np

random_observations_per_sample = 1000
num_samples = 2000
s = []

for _ in xrange(num_samples):
    total = 0
    for __ in xrange(random_observations_per_sample):
        total += random.random()

    mean = total / random_observations_per_sample
    s.append(mean)

plt.hist(s, range=(min(s), max(s)), bins=20 )
plt.show()
