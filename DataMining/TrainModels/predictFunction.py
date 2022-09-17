import pickle


# noinspection PyPep8Naming
def predictResult(elements, modelFileName):
    modelFile = open(modelFileName, 'rb')
    model = pickle.load(modelFile)
    results = model.predict(elements)
    results = list(map(lambda x: 'No' if (x == 0) else 'Yes', results))
    return results
