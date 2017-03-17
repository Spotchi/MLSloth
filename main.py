# CRISP-DM Python template, main
#import logging
import load
#import Model.svm.model as svmimport imp
import cDataPreparation.dataCleaning.cleaningFunctions as clean
import cDataPreparation.dataConstruction.constructFunctions as construct

from sklearn.datasets import fetch_20newsgroups

#import DataPreparation.integrating

pathToSelectedData = "./_data/raw/train.json"              # Where the initial data can be found
rawDataType = 'json'
label = 'firstLabel'
pathToCleanData = "./data/clean/"               # Where different versions of the cleaned data can be found
pathToConstructedData = "./data/constructed/"   # Where different versions of the constructed data can be found

cleanDataFunctionToUse = clean.decode
constructDataFunctionToUse = construct.buildTfIdfMatrix

#data = {version:.., tables:.., functionUsed:..., rawDataUsed: ...}

cleanData = load.conditionalLoadCleanData(clean.identity, pathToSelectedData, label, rawDataType)
constructData = load.conditionalLoadConstructData(constructDataFunctionToUse, cleanData)
print(constructData[1:5])

#ABT = integrateData(cleanData, constructData)

#modelingGrid = list()
# TODO load configurations from other files, check if they have been run or not,
# TODO config file that says which configs have been run
#modelingGrid.append({construct: constructDataFunctionToUse, model:modelOptions})

## TODO implement the functions on the recipes problem
#for params in modelingGrid:
#    if dataHasChangedSinceLastTask:
#        constructData = conditionalLoadConstructData(constructDataFunctionToUse)
#    ABT = integrateData(cleanData, constructData)
#    trainABT, validationABT = testDesign(ABT, testOptions)
#    model = modelType(modelOptions, ABT)
#    assessment = modelAssessment(model, validation)
#    logging.logAndSave(model, modelOptions, assessment, cleanDataFunctionToUse, constructDataFunctionToUse)
