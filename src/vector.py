

words = input()
seg_list = jieba.cut_for_search(words)
size = 0
vector_word = list()
for i in seg_list:
    size += 1
    vector_word.append(i)
print(vector_word)
vecotor_q = np.zeros(size)
# print(vecotor_q)
with open('./rverIndex.json', 'r', encoding='utf8') as fp:
    json_data = json.load(fp)
k = 0
while k < size:
    if vector_word[k] in json_data:
        vecotor_q[k] += 1
        k += 1
    else:
        k += 1
print(vecotor_q)




