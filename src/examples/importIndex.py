import os
import jieba
import json
# DEFINES
docDir = '../../data/docs'
indexDir = '../../data/index'
fileList = []

# print(os.path.dirname(os.path.abspath(__file__)))
docDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), docDir)
indexDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), indexDir)

with open(os.path.join(indexDir, 'rverIndex.json'), 'r') as jfd:
    tempdict = json.load(jfd)

print(tempdict['共产']['../data/docs/毛泽东选集/毛泽东-湖南农民运动考察报告.txt'])
