import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

sphist = pd.read_csv('sphist.csv',',')

#lets change the Date columns to datetime datatype
sphist['Date'] = pd.to_datetime(sphist['Date'])
#date_gt_20150401 = sphist['Date'] > datetime(year=2015,month=4,day=1)

#sort the data
sphist.sort_values('Date',inplace=True)

'''for i in range(0,len(sphist)):
    # load 0 for less t5
    if i < i5:
        sphist['day-5'].iloc[i] = 0
    else:
        #print(sphist['Close'].iloc[i-5:i])
        sphist['day-5'].iloc[i] = np.mean(sphist['Close'].iloc[i-5:i])
    if i < i30:
        sphist['day-30'].iloc[i] = 0
    if i < i365:
        sphist['day-365'].iloc[i] = 0
'''
cols =['5','30','365']
for col in cols:
    sphist['day-' + col] = sphist['Close'].rolling(window=int(col),min_periods=int(col)).mean()
    sphist['day-' + col] = sphist['day-' + col].shift(1)
    sphist['day-' + col].fillna(value=0,inplace=True)
    
    sphist['std-' + col] = sphist['Close'].rolling(window=int(col),min_periods=int(col)).std() 
    sphist['std-' + col] = sphist['std-' + col].shift(1)
    sphist['std-' + col].fillna(value=0,inplace=True)
    
sphist['rat-d5-d365']= sphist['rat-s5-s365'] = 0 
sphist['rat-d5-d365'][365:]= sphist['day-5'][365:]/sphist['day-365'][365:]
sphist['rat-s5-s365'][365:]= sphist['std-5'][365:]/sphist['std-365'][365:]

sphist = sphist[sphist['Date'] >= datetime(year=1951,month=6,day=19)] 
train = sphist[sphist['Date'] < datetime(year=2013,month=1,day=1)]
test = sphist[sphist['Date'] >= datetime(year=2013,month=1,day=1)]

features=['day-5','day-30','day-365','std-5','std-30','std-365','rat-d5-d365','rat-s5-s365']
target='Close'

lr = LinearRegression()
lr.fit(train[features],train[target])
predictions = lr.predict(test[features])
mae = mean_absolute_error(predictions,test[target])

print(predictions[-5:],sphist['Close'].tail(5)) 
print(mae)