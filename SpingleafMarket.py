# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:40:15 2015

@author: weizhi
"""

import pandas as pd

train = pd.read_csv('/Users/weizhi/Downloads/kaggle competion/train.csv')

#sample_submit = pd.read_csv('/Users/weizhi/Downloads/kaggle competion/sample_submission.csv')
count =0
count1 = 0
X = train.iloc[:,:-1]
y = train.iloc[:,-1]
numberFeature = []
stringFeature = []
train = []
for types in X.dtypes:
    if types == 'int64' or types== 'float':
        count+=1
        numberFeature.append(count)
    if types =='object':
        count1+=1
        stringFeature.append(count1)
print count
print count1

numberFeatures =X.iloc[:,numberFeature]
#X = []
stringFeature = X.iloc[:,stringFeature]
X = []

#%% Adaboosting classifcations trees

from sklearn.ensemble import AdaBoostClassifier 

bdt = AdaBoostClassifier()

bdt.fit(numberFeatures,y)














#%% Deep Learning
#from lasagne.layers import DenseLayer
#from lasagne.layers import InputLayer
#from lasagne.layers import DropoutLayer
#from lasagne.nonlinearities import softmax
#from lasagne.updates import nesterov_momentum
#from nolearn.lasagne import NeuralNet
#
#from matplotlib.colors import ListedColormap
#from sklearn.metrics import roc_curve, auc
#import numpy as np
#from matplotlib import pyplot as plt
#
#from sklearn.preprocessing import LabelEncoder
#from scipy import interp
#
#encoder = LabelEncoder()
#    
#layers0 = [('input', InputLayer),
#           ('dense0', DenseLayer),
#          # ('dropout', DropoutLayer),
#           ('dense1', DenseLayer),
#           ('dense2',DenseLayer),
#           ('output', DenseLayer)]
#
#net0 = NeuralNet(layers=layers0,
#                 
#                 input_shape=(None, 2),
#                 dense0_num_units=50,
#               #  dropout_p=0.5,
#                 dense1_num_units=50,
#                 dense2_num_units=50,
#                 output_num_units=2,
#                 output_nonlinearity=softmax,
#                 
#                 update=nesterov_momentum,
#                 update_learning_rate=0.01,
#                 update_momentum=0.9,
#                 
#                 eval_size=0.2,
#                 verbose=1,
#                 max_epochs=1000)
#from sklearn.preprocessing import LabelEncoder
#encoder = LabelEncoder()
#y_train = encoder.fit_transform(y).astype(np.int32)
#y =[]
#net0.fit(numberFeatures,y_train) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 