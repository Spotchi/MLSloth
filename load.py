import json

# TODO
def doesDataExist(label):
    return False, None

def loadCleanData(cleanDataPath):
    return None

def conditionalLoadCleanData(cleanDataFunctionToUse, rawDataPath, label, dataType):
    cleanDataExists, cleanDataPath = doesDataExist(label)
    if cleanDataExists:
        print("Loading cleaned data...")
        return loadCleanData(cleanDataPath)
    if not cleanDataExists:
        print("Loading raw data...")
        raw = loadRawData(rawDataPath, dataType)
        print("Cleaning raw data...")
    return cleanDataFunctionToUse(raw)

def conditionalLoadConstructData(constructDataFunctionToUse, cleanData):
    print("Loading constructed data...")
    return constructDataFunctionToUse(cleanData)

def loadRawData(filePath, dataType):
    if dataType == 'json':
        with open(filePath, 'rt', encoding='utf-8') as json_data:
            return json.load(json_data)
    
