import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.formula.api as smf

# Load the data
fulldata = pd.read_csv('london_crime.csv')

# Create crimerate and policerate
fulldata['crimerate'] = fulldata['crime'] / fulldata['population']
fulldata['policerate'] = fulldata['police'] / fulldata['population']

# Log-transform the variables
fulldata['lcrime'] = np.log(fulldata['crimerate'])
fulldata['lpolice'] = np.log(fulldata['policerate'])
fulldata['lemp'] = np.log(fulldata['emp'])
fulldata['lun'] = np.log(fulldata['un'])
fulldata['lymale'] = np.log(fulldata['ymale'])
fulldata['lwhite'] = np.log(fulldata['white'])

# Prepare features and target for ML models
features = fulldata[['lpolice', 'lun', 'lemp', 'lymale', 'lwhite']]
target = fulldata['lcrime']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Linear Regression Model
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
lin_preds = lin_reg.predict(X_test)

# Evaluate Linear Regression
lin_mse = mean_squared_error(y_test, lin_preds)
lin_r2 = r2_score(y_test, lin_preds)
print("Linear Regression Results:")
print(f"MSE: {lin_mse}")
print(f"R^2: {lin_r2}")

# Random Forest Regressor
rf_reg = RandomForestRegressor(random_state=42)
rf_reg.fit(X_train, y_train)
rf_preds = rf_reg.predict(X_test)

# Evaluate Random Forest
rf_mse = mean_squared_error(y_test, rf_preds)
rf_r2 = r2_score(y_test, rf_preds)
print("\nRandom Forest Results:")
print(f"MSE: {rf_mse}")
print(f"R^2: {rf_r2}")

# Statsmodels Log-Log Regression
model1 = smf.ols('lcrime ~ lpolice + lun + lemp + lymale + lwhite', data=fulldata).fit()
print("\nStatsmodels Log-Log Regression Results:")
print(model1.summary())

# Differenced Data
year1 = fulldata[fulldata['week'] <= 52].copy()
year2 = fulldata[fulldata['week'] > 52].copy()

year1.sort_values(['borough', 'week'], inplace=True)
year2.sort_values(['borough', 'week'], inplace=True)

diffdata = pd.DataFrame()
diffdata['dlcrime'] = year2['lcrime'].values - year1['lcrime'].values
diffdata['dlpolice'] = year2['lpolice'].values - year1['lpolice'].values
diffdata['dlun'] = year2['lun'].values - year1['lun'].values
diffdata['dlemp'] = year2['lemp'].values - year1['lemp'].values
diffdata['dlymale'] = year2['lymale'].values - year1['lymale'].values
diffdata['dlwhite'] = year2['lwhite'].values - year1['lwhite'].values
diffdata['week'] = year2['week'].values

# Natural Experiment Variables
diffdata['sixweeks'] = ((diffdata['week'] >= 80) & (diffdata['week'] <= 85)).astype(int)
year2_boroughs = year2['borough'].values
treated_boroughs = [1, 2, 3, 6, 14]
diffdata['sixweeks_treat'] = ((diffdata['week'] >= 80) & (diffdata['week'] <= 85) & np.isin(year2_boroughs, treated_boroughs)).astype(int)

# Statsmodels Differenced Regression
model2 = smf.ols('dlcrime ~ dlpolice + dlun + dlemp + dlymale + dlwhite + C(week)', data=diffdata).fit()
print("\nDifferenced Regression Results:")
print(model2.summary())

# Statsmodels Natural Experiment
model3 = smf.ols('dlcrime ~ dlun + dlemp + dlymale + dlwhite + sixweeks + sixweeks_treat + C(week)', data=diffdata).fit()
print("\nNatural Experiment Regression Results:")
print(model3.summary())
