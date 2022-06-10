# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import json
from unicodedata import name
import numpy as np
import jieba
import os
import collections
import logging
# 按间距中的绿色按钮以运行脚本。


def inputVector():
    print('input:')
    jieba.setLogLevel(logging.INFO)
    words = input()
    seg_list = jieba.lcut_for_search(words)
    words_not_in_dic = set()
    # print(vector_word)
    # print(os.getcwd())
    with open('./data/index/rverIndex.json', 'r', encoding='utf8') as fp:
        json_data = json.load(fp)
        vecotor_q = np.zeros(len(json_data))

    new_dict = json_data

    for key in new_dict.keys():
        new_dict[key] = 0

    for word in seg_list:
        try:
            new_dict[word] += 1
        except:
            words_not_in_dic.add(word)

    new_dict = collections.OrderedDict(
        sorted(new_dict.items(), key=lambda t: t[0]))
    # print(new_dict)
    return new_dict


if __name__ == '__main__':
    inputvec = inputVector()
    print(inputvec)
    path = './data/index/fileFreq.json'
    with open(path, 'r') as dataset:
        filevec = json.load(dataset)
