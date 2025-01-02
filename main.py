import pandas as pd
import functions as f

insuranceTrainingDataset = pd.read_csv("train.csv")
insuranceTrainingDataset = f.fillMissingData(insuranceTrainingDataset)

# insuranceTrainingDataset = insuranceTrainingDataset.dropna()

encodedInsuranceTrainingDataset = pd.get_dummies(insuranceTrainingDataset, columns = ['Gender', 'Marital Status', 'Education Level', 'Occupation', 'Location', 'Policy Type', 'Customer Feedback', 'Smoking Status', 'Exercise Frequency', 'Property Type'])

encodedInsuranceTrainingDataset['Policy Start Date'] = pd.to_datetime(encodedInsuranceTrainingDataset['Policy Start Date']).astype('int64')

from sklearn.preprocessing import StandardScaler
y = encodedInsuranceTrainingDataset['Premium Amount']

scaler = StandardScaler()
x = scaler.fit_transform(encodedInsuranceTrainingDataset.drop(['id', 'Premium Amount'], axis=1))

import xgboost as xgb
from sklearn.model_selection import train_test_split

model = xgb.XGBRegressor()

model.fit(x, y)

insuranceTestingDataset = pd.read_csv("test.csv")
insuranceTestingDataset = f.fillMissingData(insuranceTestingDataset)
encodedInsuranceTestingDataset = pd.get_dummies(insuranceTestingDataset, columns = ['Gender', 'Marital Status', 'Education Level', 'Occupation', 'Location', 'Policy Type', 'Customer Feedback', 'Smoking Status', 'Exercise Frequency', 'Property Type'])

encodedInsuranceTestingDataset['Policy Start Date'] = pd.to_datetime(encodedInsuranceTestingDataset['Policy Start Date']).astype('int64')

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_test = scaler.fit_transform(encodedInsuranceTestingDataset.drop(['id'], axis=1))

y_pred = model.predict(x_test)

result = []
for i in range(len(y_pred)):
    result.append([encodedInsuranceTestingDataset['id'][i], y_pred[i]])
resultData = pd.DataFrame(result, columns = ['id', 'Premium Amount'])
resultData.to_csv('result.csv', index=False)
