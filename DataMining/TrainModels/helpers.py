from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import os.path
from datetime import datetime
import json
import pickle


# noinspection PyPep8Naming
def calculateScores(y_test, y_pred):
    scores = {'Accuracy': accuracy_score(y_test, y_pred), 'Precision': precision_score(y_test, y_pred),
              'Recall': recall_score(y_test, y_pred), 'F1': f1_score(y_test, y_pred),
              'AUC': roc_auc_score(y_test, y_pred)}
    return scores


# noinspection PyPep8Naming
def formatScores(scores):
    for key in scores:
        scores[key] = '{:.2f}'.format(100 * scores[key])


# noinspection PyPep8Naming
def printScores(scores, withHeader=False):
    printString = ""
    if withHeader:
        for key in scores:
            printString += "{:^15} |".format(key)
        printString += "\n-------------------------------------------------------------------------------------\n"
    for key in scores:
        printString += "{:^15} |".format(scores[key])
    print(printString)


# noinspection PyPep8Naming
def printAllScores(allScores):
    table = '{:10} '.format("")
    for key in allScores:
        table += "| {:^20}".format(key)
    table += "\n------------------------------------------------------------------------------------" \
             "-------------------------------------"
    for criteriaKey in allScores[list(allScores.keys())[0]]:
        table += "\n{:10} ".format(criteriaKey)
        for algorithmKey in allScores:
            table += "| {:^20}".format(allScores[algorithmKey][criteriaKey])
    table += "\n------------------------------------------------------------------------------------" \
             "-------------------------------------"
    print(table)


# noinspection PyPep8Naming
def saveScoresInFile(allScores):
    folder = 'allTimesTrainedScores'
    if not os.path.exists(folder):
        os.makedirs(folder)
    now = datetime.now()
    now = now.strftime("%Y-%m-%dT%I_%M_%p")
    jsonString = json.dumps(allScores)
    fileName = f"{folder}/{now}.json"
    jsonFile = open(fileName, "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    return fileName


# noinspection PyPep8Naming
def getScoresJsonObjectFromSavedFile(fileName):
    # open json file
    openedFile = open(f'allTimesTrainedScores/{fileName}.json')
    # read file as json object
    scores = json.load(openedFile)
    return scores


# noinspection PyPep8Naming
def saveModel(fileName, model):
    folder = 'TrainedModels'
    if not os.path.exists(folder):
        os.makedirs(folder)
    file = open(f'{folder}/{fileName}', 'wb')
    pickle.dump(model, file)
    file.close()
