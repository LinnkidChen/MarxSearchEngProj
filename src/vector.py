# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import json
from unicodedata import name
import numpy as np
import jieba
import collections

# 按间距中的绿色按钮以运行脚本。


def inputVector():
    words = input()
    seg_list = jieba.lcut_for_search(words)
    size = 0
    vector_word = list()
    for i in seg_list:
        size += 1
        vector_word.append(i)
    print(vector_word)

    with open('data/index/rverIndex.json', 'r', encoding='utf8') as fp:
        json_data = json.load(fp)
        vecotor_q = np.zeros(len(json_data))

    new_dict = json_data

    for key in new_dict.keys():
        new_dict[key] = 0

    for word in seg_list:
        new_dict[word] += 1
    new_dict = collections.OrderedDict(
        sorted(new_dict.items(), key=lambda t: t[0]))
    print(new_dict)
    return vecotor_q
