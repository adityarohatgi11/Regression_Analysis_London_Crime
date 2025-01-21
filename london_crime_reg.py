import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

#Load the data
fulldata = pd.read_csv('london_crime.csv')

#Part 1: Log-Log Regression
#Create crimerate and policerate
fulldata['crimerate'] = fulldata['crime'] / fulldata['population']
fulldata['policerate'] = fulldata['police'] / fulldata['population']

#Log-transform the variables
fulldata['lcrime'] = np.log(fulldata['crimerate'])
fulldata['lpolice'] = np.log(fulldata['policerate'])
fulldata['lemp'] = np.log(fulldata['emp'])
fulldata['lun'] = np.log(fulldata['un'])
fulldata['lymale'] = np.log(fulldata['ymale'])
fulldata['lwhite'] = np.log(fulldata['white'])

#Running the regression
model1 = smf.ols('lcrime ~ lpolice + lun + lemp + lymale + lwhite', data=fulldata).fit()
print("Part 1: Log-Log Regression Results")
print(model1.summary())

#Part 2: Differenced Regression
#Split the data into Year 1 and Year 2 based on weeks
year1 = fulldata[fulldata['week'] <= 52].copy()
year2 = fulldata[fulldata['week'] > 52].copy()

#Sorting Data
year1.sort_values(['borough', 'week'], inplace=True)
year2.sort_values(['borough', 'week'], inplace=True)

#Calculate the differenced variablesp
diffdata = pd.DataFrame()
diffdata['dlcrime'] = year2['lcrime'].values - year1['lcrime'].values
diffdata['dlpolice'] = year2['lpolice'].values - year1['lpolice'].values
diffdata['dlun'] = year2['lun'].values - year1['lun'].values
diffdata['dlemp'] = year2['lemp'].values - year1['lemp'].values
diffdata['dlymale'] = year2['lymale'].values - year1['lymale'].values
diffdata['dlwhite'] = year2['lwhite'].values - year1['lwhite'].values
diffdata['week'] = year2['week'].values

#Running the regression
model2 = smf.ols('dlcrime ~ dlpolice + dlun + dlemp + dlymale + dlwhite + C(week)', data=diffdata).fit()
print("\nPart 2: Differenced Regression Results")
print(model2.summary())

#Part 3: Natural Experiment
#Create the dummy variables for sixweeks and sixweeks_treat
diffdata['sixweeks'] = ((diffdata['week'] >= 80) & (diffdata['week'] <= 85)).astype(int)

#Values of boroughs from the diffdata
year2_boroughs = year2['borough'].values
treated_boroughs = [1, 2, 3, 6, 14]
diffdata['sixweeks_treat'] = ((diffdata['week'] >= 80) & (diffdata['week'] <= 85) & np.isin(year2_boroughs, treated_boroughs)).astype(int)

#Running the regression
model3 = smf.ols('dlcrime ~ dlun + dlemp + dlymale + dlwhite + sixweeks + sixweeks_treat + C(week)', data=diffdata).fit()
print("\nPart 3: Natural Experiment Regression Results")
print(model3.summary())
