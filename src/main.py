from vector import inputVector
from vector import word_in
import json
import numpy as np
import heapq
import jieba
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
    # 输入quit退出循环
    global word_in
    while True:
        inputvec = inputVector()
        if inputvec is None:
            break
        inputvec = list(inputvec.values())
        inputvec = np.array(inputvec).reshape(-1, 1)
        # print(inputvec)
        with open("/MarxSearchEngProj/data/index/fileFreqAddr.json", 'r') as fd:
            fileFreqArr = np.array(json.load(fd))
        fileFreqArr_norm = norm_l2(fileFreqArr)
        inputvec_norm = norm_l2(inputvec)
        relVec = fileFreqArr.dot(inputvec)
        relVec_norm = fileFreqArr_norm.dot(inputvec_norm)
        np_relVec_norm2 = np.array(relVec_norm)
        np_relVec_norm = np_relVec_norm2.flatten()
        # print(np_relVec_norm)
        max_indexs = heapq.nlargest(5, range(len(np_relVec_norm)), np_relVec_norm.take)
        print(max_indexs)
        with open("/MarxSearchEngProj/data/index/fileList.json", 'r', encoding='utf8') as fd1:
            fileList = np.array(json.load(fd1))

        with open("/MarxSearchEngProj/data/index/rverIndex.json", 'r', encoding='utf8') as fd2:
            rverIndex = json.load(fd2)
        for i in max_indexs:
            print("相关度: ",np_relVec_norm[i],fileList[i], end=' ')
            path = str(fileList[i]).split(':')[5].replace('}','').replace('\'','').replace(' ','')
            # print(path)
            # print(rverIndex['马克思'][path])
            print("主要匹配内容：", end='')
            for word in word_in:
                if path in rverIndex[word]:
                    print(word,end='、')
            print()
        print(word_in)





