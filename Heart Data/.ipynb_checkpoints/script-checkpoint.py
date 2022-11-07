import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler

sns.set()

file = './heart.csv'

df = pd.read_csv(file)
df_dummies = pd.get_dummies(data=df).drop(columns=['Sex_F', 'ExerciseAngina_N'])
df_dummies = df_dummies[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak',
                         'Sex_M', 'ChestPainType_ASY', 'ChestPainType_ATA',
                         'ChestPainType_NAP', 'ChestPainType_TA', 'RestingECG_LVH',
                         'RestingECG_Normal', 'RestingECG_ST', 'ExerciseAngina_Y',
                         'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up', 'HeartDisease']]

data = df_dummies.drop(columns=['HeartDisease']).to_numpy()
target = df_dummies['HeartDisease']

scaler = MinMaxScaler(feature_range=(0, 1))
scaledData = scaler.fit_transform(data)

model = LogisticRegression()
model.fit(scaledData, target)
