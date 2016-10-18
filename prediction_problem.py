# -*- coding: utf-8 -*-
"""
Created on Sat May 07 16:29:39 2016

@author: MaGesh
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt 

from datetime import datetime
from matplotlib.dates import MonthLocator, DateFormatter

from sklearn.preprocessing import StandardScaler

inputFile = pd.read_csv('\data') #This input had extra 50 columns as whitespaces so I had to delete it 

train = inputFile.ix[:49,:]
test=inputFile.ix[50:,:]
date=inputFile['date']

train=train.drop(['date'],axis=1)
test=test.drop(['date','S1'],axis=1)
y=train['S1'].astype(np.float32)
train=train.drop(['S1'],axis=1)

######## check whether the data is linear################
#plt.scatter(train['S7'], train['S1'])
#plt.xlabel('S7')
#plt.ylabel('S1')
#plt.show()

######### PRE PROCESSING ########

train = StandardScaler().fit_transform(train)
train=train.astype(np.float32)


test = StandardScaler().fit_transform(test)
test=test.astype(np.float32)

######## RF MODEL ########
rf=  RandomForestRegressor(n_estimators=150, max_depth=15)
rf.fit(train, y)


######## FEATURE IMPORTANCE ########

importances= rf.feature_importances_
indices = np.argsort(importances)[::-1]
for f in range(train.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

######## PREDICTION ########
pred = rf.predict(test)
#clf=GridSearchCV(SVR(kernel='linear',C=1.0, epsilon=0.2,))

#svr=SVR(kernel='linear', gamma='auto',C=1.0,epsilon=0.1)
#svr.fit(train_test, y_train)
#predSVR= svr.predict(test_test)

#final_pred = predSVR * 0.5 + pred * 0.5

#print "R2Score:" (r2_score(y_true,pred))

######## WRITING PREDICTED VALUES TO CSV FILE ########
finalValue= np.concatenate((y,pred),axis=0)
print finalValue.shape
pred = pd.DataFrame(finalValue,columns=['S1'])
pred = pd.concat([date,pred],axis=1)
pred.to_csv('data\predictions.csv',index=False)


######## PLOTTING S1 vs Months ########
dateString = pred['date']
dateV=[]
for i in dateString:
    datetime_obj = datetime.strptime(i, '%m/%d/%Y %H:%M')
    dateV.append(datetime_obj)


monthsFmt=DateFormatter('%m')
monthLocator = MonthLocator()
fig, ax = plt.subplots()
ax.plot_date(dateV, pred['S1'], '-')
ax.xaxis.set_major_locator(monthLocator)
ax.xaxis.set_major_formatter(monthsFmt)
ax.autoscale_view()
ax.grid(True)
plt.xlabel("Months")
plt.ylabel("Stocks (S1)")
plt.show()

######## END OF PROGRAM ########