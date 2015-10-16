# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:40:15 2015

@author: weizhi
"""

import pandas as pd

train = pd.read_csv('/Users/weizhi/Downloads/kaggle competion/train.csv')

sample_submit = pd.read_csv('/Users/weizhi/Downloads/kaggle competion/sample_submission.csv')
count =0
count1 = 0
X = train.iloc[:,:-1]
y = train.iloc[:,-1]
numberFeature = []
stringFeature = []
train = []
for types in X.dtypes:
    if types == 'int64' or types== 'float':
        numberFeature.append(count)
    if types =='object':
        stringFeature.append(count)
    count +=1
print count


numberFeatures =X.iloc[:,numberFeature]
#X = []
stringFeature = X.iloc[:,stringFeature]
X = []
#%%
import pylab as plt
plt.figure()
plt.plot(numberFeatures.iloc[:,4])


def plotCorr(data,number):
    subData = data.iloc[number*1000:(number+1)*1000,:]
    corrY = subData.corr()
    plt.figure()
    plt.imshow(corrY)

plotCorr(numberFeatures,1)
plotCorr(numberFeatures,2)

#%%
from sklearn.feature_extraction import FeatureHasher
hasher = FeatureHasher(input_type='string',dtype='float')
strFeature = hasher.fit_transform(stringFeature)

#%% normalizetoin
numberFeatures = numberFeatures.fillna(0)

from sklearn import preprocessing
scaler = preprocessing.StandardScaler().fit(numberFeatures.iloc[:,1:])
X_scaled = scaler.transform(numberFeatures.iloc[:,1:])
import numpy as np
#a = numpy.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
#numpy.savetxt("/Users/weizhi/Downloads/kaggle competion/scared.csv", X_scaled, delimiter=",")

where_are_NaNs = np.isnan(X_scaled)
X_scaled[where_are_NaNs] = 0
#data = pd.read_csv("/Users/weizhi/Downloads/kaggle competion/scared.csv")
numberFeatures = None
import random 
index = random.sample(range(X_scaled.shape[0]),  10000)

trainSample = X_scaled[index,:]
target = y.iloc[index]



#%%


from sklearn.ensemble import ExtraTreesClassifier
clf1 = ExtraTreesClassifier(n_estimators = 500, max_features = 'sqrt',max_depth=4,min_samples_split=4,random_state=369)
clf1.fit(trainSample, target)
importances = clf1.feature_importances_
indices = np.argsort(importances)[::-1]

#%% train SVM 

from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4,1e-5],
                     'C': [ 10, 100, 1000]}]

#clf = GridSearchCV(SVC(C=1), tuned_parameters)
clf = SVC(gamma = 0.01,random_state=368,C=10,probability=True)
clf.fit(trainSample[:,indices[:100]], target)

#%% xgboost

import xgboost as xg


param = {"objective" : "multi:softprob",
"eval_metric" : "mlogloss",
"num_class" : 9,
"gamma" : 0,
"nthread" : 8,
"eta" : 0.05,
"max_depth" : 12,
"min_child_weight" : 4,
"subsample" : .9,
"colsample_bytree" : .8}

xgb_model = xg.XGBClassifier(learning_rate=0.1, n_estimators=100, silent=True, objective="multi:softprob",
                 nthread=-1, max_delta_step=0, subsample=.9, colsample_bytree=.8,
                 base_score=0.5, seed=0)

clf = GridSearchCV(xgb_model,
                   {'max_depth': [6,8,10,12,14],
                    'n_estimators': [100,200,250],'gamma':[0.1,0,1],'min_child_weight':[4,6,8]}, verbose=1,cv=10)

clf.fit(X.values,yy.values)

clf.best_estimator_

#%% reading the test data
test = pd.read_csv('/Users/weizhi/Downloads/kaggle competion/test.csv')
test = test.fillna(0)
testData = test.iloc[:,numberFeature]
test = None
Test_scaled = scaler.transform(testData.iloc[:,1:])
where_are_NaNs = np.isnan(Test_scaled)
Test_scaled[where_are_NaNs] = 0
testData =None

#%% result
result = clf1.predict_proba(Test_scaled)

result_svm = clf.predict_proba(Test_scaled[:,indices[:100]])
#Test_scaled = None

#%% from kaggle
data = pd.read_csv('/Users/weizhi/Downloads/xgb3.csv')

sample_submit['target'] = 0.1*result[:,1] + 0.65*data['target'] + 0.3*result_svm[:,1]
#sample_submit['target'] = result_svm[:,1]
sample_submit.to_csv('/Users/weizhi/Downloads/kaggle competion/sample_submission_SVM_RF_SVM.csv',index=False)







