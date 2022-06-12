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

word_in = list()

def inputVector():
    print('input:')

    global word_in
    jieba.setLogLevel(logging.INFO)
    words = input()
    if words == 'quit':
        return

    word_in.clear()
    seg_list = jieba.lcut_for_search(words)
    for i in seg_list:
        word_in.append(i)
    words_not_in_dic = set()
    # print(vector_word)
    # print(os.getcwd())
    with open('/MarxSearchEngProj/data/index/rverIndex.json', 'r', encoding='utf8') as fp:
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

# 输入quit退出循环
    while True:
        inputvec = inputVector()
        if inputvec is None:
            break
        print(inputvec)
        path = '/MarxSearchEngProj/data/index/fileFreq.json'
        with open(path, 'r', encoding='utf8') as dataset:
            filevec = json.load(dataset)
        # print(filevec['../data/docs/马克思/马克思-工人联合会.txt'])



