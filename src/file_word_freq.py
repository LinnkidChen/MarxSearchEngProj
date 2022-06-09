import json
from typing import Dict, List, Tuple
import os


def get_file_word_freq(path) -> Dict[str, Dict[str, int]]:
    file_dict = {}
    with open(path, 'r') as dataset:
        json_data = json.load(dataset)
        for word in json_data:
            word_file_list = json_data[word]
            for file_name in word_file_list:
                freq_arr = word_file_list[file_name]
                if file_dict.get(file_name) is None:
                    file_dict[file_name] = {}
                file_dict[file_name][word] = len(freq_arr)
    return file_dict


def get_file_word_freq2(path: str) -> Dict[str, Dict[str, int]]:
    file_dict = {}
    bucket = set()
    with open(path, 'r') as dataset:
        json_data = json.load(dataset)
        for word in json_data:
            bucket.add(word)
            word_file_list = json_data[word]
            for file_name in word_file_list:
                freq_arr = word_file_list[file_name]
                if file_dict.get(file_name) is None:
                    file_dict[file_name] = {}
                file_dict[file_name][word] = len(freq_arr)

    for file_name in file_dict:
        for word in bucket:
            if file_dict[file_name].get(word) is None:
                file_dict[file_name][word] = 0

    return file_dict


if __name__ == '__main__':
    indexDir = 'data/index'
    file_word_freq = get_file_word_freq2(
        "data/index/rverIndex.json")
    with open(os.path.join(indexDir, 'fileFreq.json'), 'w') as jfd:
        json.dump(file_word_freq, jfd, ensure_ascii=False)
    # print(file_word_freq)
