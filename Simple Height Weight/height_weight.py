"""
Simple height & weight ML model
Predict weight(lbs) using height(inches)
Author: Obinna Jason Nwoke II
Source: http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

sample = pd.read_excel('sample.xlsx')
sample.drop(columns=['Index'], inplace=True)

data = np.array(sample['Height(Inches)']).reshape(-1, 1)
target = np.array(sample['Weight(Pounds)'])

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=.2)
model = LinearRegression(fit_intercept=True)

# creating the line of best fit
prediction_space = np.linspace(min(data), max(data)).reshape(-1, 1)

model.fit(data, target)
predicted_heights = model.predict(prediction_space)

print("Model Score: {}".format(model.score(data, target)))

sns.scatterplot(data=sample, x='Height(Inches)', y='Weight(Pounds)')
plt.plot(prediction_space, predicted_heights, color='black', linewidth=3)
# plt.show()

sample['Predicted Weight'] = model.predict(data)
print(sample)
