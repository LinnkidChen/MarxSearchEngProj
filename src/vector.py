# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import json
import numpy as np
import jieba


# 按间距中的绿色按钮以运行脚本。

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


mydict = dict()

loc = 0
for j in json_data:
    mydict[j] = loc
    loc += 1

# print(mydict)
k = 0

while k < size:
    if vector_word[k] in json_data:
        vecotor_q[mydict[vector_word[k]]] += 1
        k += 1
    else:
        k += 1
print(vecotor_q)
