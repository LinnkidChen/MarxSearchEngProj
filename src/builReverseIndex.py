import os
import jieba
import json
import logging


def validIndex(text):
    # for python 3.x
    # sample: ishan('一') == True, ishan('我&&你') == False
    return all('\u4e00' <= char <= '\u9fff' or u'\u0039' >= char >= u'\u0030' or u'\u005a' >= char >= u'\u0041' for char in text)


def buildReverseIndex():
    jieba.setLogLevel(logging.INFO)
    # DEFINES
    docDir = './data/docs'
    indexDir = './data/index'
    fileList = []
    # docDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), docDir)
    # indexDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), indexDir)

    # print(fileList)

    for root, dirs, files in os.walk(docDir):
        for name in files:
            tempPath = os.path.join(root, name)
            # print(tempPath)
            if tempPath[-3:] == 'txt':
                fileList.append(os.path.join(root, name))
                # print(1)

    with open(os.path.join(indexDir, 'fileList.json'), 'w') as fd:
        json.dump(fileList, fd, ensure_ascii=False)

    index_dict = {}

    for file in fileList[0:30]:
        fd = open(file, "r")
        lineCount = 1
        for line in fd:
            seg_list = jieba.lcut_for_search(line)
            for word in seg_list:
                if validIndex(word):
                    try:
                        index_dict[word]
                    except:
                        index_dict[word] = {}

                    try:
                        index_dict[word][file]
                    except:
                        index_dict[word][file] = []

                    index_dict[word][file].append(lineCount)
            lineCount = lineCount+1

    with open(os.path.join(indexDir, 'rverIndex.json'), 'w') as jfd:
        json.dump(index_dict, jfd, ensure_ascii=False)
