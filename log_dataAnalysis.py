# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:17:41 2015

@author: weizhi
"""


#%% loading each files
import glob, os
# https://docs.python.org/2/library/os.html
def findFilePath(path):
    os.chdir(path)
    filePaths = []
    for file in glob.glob("*.csv"):
        filePaths.append(file)
    return filePaths

#%% hours and generate the outputs
# deal with each csv file 
import pandas as pd
class logDataAnalysis(object):
    def __init__(self,path,hour,fileName):
        self.path = path
        self.hour = hour
        self.fileName = fileName
        
    def readCSV(self,filePath):
        data = pd.read_csv(filePath)
        return data 
    def transfromTimeFormat(self,data):
        timeColumn = data[data.keys()[-1]]
        for i in range(len(timeColumn)):
            item = timeColumn.loc[i]
            T1 = item.split(' ')
            T2 = T1[1].split(':')[0]
            binTime = int(T2)/(self.hour)
            leftBin = str(binTime*(self.hour)).zfill(2)
            rightBin = str((binTime+1)*(self.hour)-1).zfill(2)
            T3 = leftBin + '_' + rightBin
            T4 = T1[0] + '_'+ T3
            timeColumn.loc[i] = T4
        data[data.keys()][-1] = timeColumn
        return data
        
    def generateOutputs(self,path):
        data = self.transfromTimeFormat(self.readCSV(path))
        keys = [key for key in data.keys()]
        keys.reverse()
        dataGroup = data.groupby(keys).groups
        keysOuput = sorted(dataGroup.iterkeys())  # keep the keys sorted rather than hashing
        outputs = pd.DataFrame(columns = ['period','content_id','uid','count'])
        count = 0
        for key in keysOuput:
            curr = list(key)   # write to each columns to outputs.csv
            curr.append(len(dataGroup[key])) # get the count of keys from groupby
            outputs.loc[count] = curr
            count +=1 
        saveFile = self.createSavePath() + '/'+'Output_'+ str(self.hour) + 'hours_'+ self.fileName
      #  print savePath
     #   saveFile = savePath 
        outputs.to_csv(saveFile,index=False)
        return outputs
    
    def createSavePath(self):
        savePath = self.path + '/' + 'Outputs'
        try:
            os.makedirs(savePath)
        except OSError:
            pass
        return savePath
    
    def mergerResult(self):
        

#%% testing
path = '/Users/weizhi/Desktop/everStringProject'
filePaths = findFilePath(path)

Obj = logDataAnalysis(path,2,filePaths[0])
data = Obj.readCSV(filePaths[0])

data.to_csv(filePaths[0],index=False)
outputs = Obj.generateOutputs(filePaths[0])


