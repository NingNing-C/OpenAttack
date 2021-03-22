"""
:type: a tuple of three :py:class:`.Dataset` s, `(train, valid, test)`.
:Size: 31.0MB

AG News dataset which is used to train victim models.
"""
import pickle

NAME = "Dataset.AG"
DOWNLOAD = "https://cdn.data.thunlp.org/TAADToolbox/dataset/sst.pkl"


def LOAD(path):
    from OpenAttack.utils import Dataset, DataInstance

    def mapping(data):
        return Dataset([
            DataInstance(
                x=it[0],
                y=it[1]
            ) for it in data
        ], copy=False)

    train, valid, test = pickle.load(open(path, "rb"))
    return mapping(train), mapping(valid), mapping(test)
