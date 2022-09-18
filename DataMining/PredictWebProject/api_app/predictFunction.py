import pickle
import os


# noinspection PyPep8Naming
def predictResult(elements, modelFileName):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelFile = open(f"{dir_path}\\TrainedModels\\{modelFileName}", 'rb')
    model = pickle.load(modelFile)
    results = model.predict(elements)
    modelFile.close()
    results = list(map(lambda x: 'No' if (x == 0) else 'Yes', results))
    return results
