import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib
import os

df = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Descriptors/training.csv')

water_features = ['mc-Z-3-all', 'D_mc-Z-3-all', 'D_mc-Z-2-all', 'D_mc-Z-1-all', 'mc-chi-3-all', 'mc-Z-1-all', 'mc-Z-0-all', 'D_mc-chi-2-all', 'f-lig-Z-2', 'GSA', 'f-lig-I-0', 'func-S-1-all']

X = df[water_features]
y = df['water_label'].apply(lambda x: 1 if x in [3, 4] else 0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(f'ROC AUC: {roc_auc}')

if not os.path.isdir('models'):
    os.mkdir('models')
joblib.dump(model, 'models/water_model.joblib')
joblib.dump(scaler, 'models/water_scaler.joblib')
