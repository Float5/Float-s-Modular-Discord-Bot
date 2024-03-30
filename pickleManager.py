import pickle

from path import getPath



def getPickle(path):
    data = None
    with open(getPath() + path, "rb") as Pickle:
        data = pickle.load(Pickle)

    if data == None:
        return 0
    else:
        return data

def setPickle(path, data):
    with open(getPath() + path, "wb") as Pickle:
        pickle.dump(data, Pickle)