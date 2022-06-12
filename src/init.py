from distutils.command.build import build
from builReverseIndex import buildReverseIndex
from vector import inputVector
import json
from file_word_freq import get_file_word_freq2
import numpy as np
from sklearn.preprocessing import normalize
import os.path


def init():
    if os.path.isfile('./data/index/fileList.json') and os.path.isfile(
            './data/index/rverIndex.json') and os.path.isfile('./data/index/fileFreqAddr.json'):
        return

    buildReverseIndex()

    # input 共产党理念资本不是本人

    # path = './data/index/fileFreq.json'
    # with open(path, 'r') as dataset:
    #     filevec = json.load(dataset)

    file_word_freq = get_file_word_freq2(
        "./data/index/rverIndex.json")

    for filename in file_word_freq.keys():
        file_word_freq[filename] = file_word_freq[filename].values()
        file_word_freq[filename] = list(file_word_freq[filename])

    # print(file_word_freq['../data/docs/马克思/马克思-共产党宣言.txt'])

    fileFreqArr = np.array(list(file_word_freq.values()))

    with open('./data/index/fileFreqAddr.json', 'w') as fd:
        json.dump(fileFreqArr.tolist(), fd)
