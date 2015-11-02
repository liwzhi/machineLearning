# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:05:54 2015

@author: weizhi


train.csv - the training set, including the columns of:
Feature_1 - Feature_25
Ret_MinusTwo, Ret_MinusOne
Ret_2 - Ret_120
Ret_121 - Ret_180: target variables
Ret_PlusOne, Ret_PlusTwo: target variables
Weight_Intraday, Weight_Daily


test.csv - the test set, including the columns of:
Feature_1 - Feature_25
Ret_MinusTwo, Ret_MinusOne
Ret_2 - Ret_120
sample_submission.csv - a sample submission file in the correct format

"""

import pandas as pd

train = pd.read_csv('/Users/weizhi/Desktop/kaggle stock data/train.csv');

test = pd.read_csv('/Users/weizhi/Desktop/kaggle stock data/test.csv');
submit = pd.read_csv('/Users/weizhi/Desktop/kaggle stock data/sample_submission.csv');

