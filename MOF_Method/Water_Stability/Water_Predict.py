import pandas as pd
import numpy as np
import joblib

water_model = joblib.load('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Model/water_model.joblib')
water_scaler = joblib.load('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Model/water_scaler.joblib')

water_features = ['mc-Z-3-all', 'D_mc-Z-3-all', 'D_mc-Z-2-all', 'D_mc-Z-1-all', 'mc-chi-3-all', 'mc-Z-1-all', 'mc-Z-0-all', 'D_mc-chi-2-all', 'f-lig-Z-2', 'GSA', 'f-lig-I-0','func-S-1-all',]

df_newMOF = pd.read_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Descriptors/CHOOH_consolidate.csv')

X_newMOF = df_newMOF[water_features]

X_newMOF = water_scaler.transform(X_newMOF)

water_pred = water_model.predict_proba(X_newMOF)[:, 1]

water_pred = np.round(water_pred, 2)

output = pd.DataFrame({'Predictions': water_pred})
output.to_csv('/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Water_Stability/Predictions/CHOOH_predict.csv', index=False)
