"""
Test suite for the model
Author: Obinna Jason Nwoke II
"""
import random
import numpy as np
import height_weight
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# sample of heights
sample = []
for i in range(100):
    sample.append(random.randint(63, 74))
new_sample = np.array(sample).reshape(-1, 1)

# predict the weights using the previous model
new_predictions = height_weight.model.predict(new_sample)

print(new_predictions)
