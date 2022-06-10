from vector import inputVector
import json
import numpy as np
from init import init
from sklearn.preprocessing import normalize


def norm_l1(array):
    x = normalize(array, norm='l1')
    return x


def norm_l2(array):
    x = normalize(array, norm='l2')
    return x


if __name__ == '__main__':
    # init()  # TODO  如果已经初始化 则不运行，并且写一个清除index的函数
    inputvec = inputVector()
    inputvec = list(inputvec.values())
    inputvec = np.array(inputvec).reshape(-1, 1)
    # print(inputvec)
    with open("./data/index/fileFreqAddr.json", 'r') as fd:
        fileFreqArr = np.array(json.load(fd))
    fileFreqArr_norm = norm_l2(fileFreqArr)
    inputvec_norm = norm_l2(inputvec)

    relVec = fileFreqArr.dot(inputvec)

    relVec_norm = fileFreqArr_norm.dot(inputvec_norm)
