import json
from typing import Dict, List, Tuple


def get_file_word_freq(path: str) -> Dict[str, List[Tuple[str, int]]]:
    file_dict = {}
    with open(path, 'r') as dataset:
        json_data: object = json.load(dataset)
        for word in json_data:
            word_file_list = json_data[word]
            for file_name in word_file_list:
                freq_arr = word_file_list[file_name]
                if file_dict.get(file_name) is None:
                    file_dict[file_name] = []
                file_dict[file_name].append((word, len(freq_arr)))
    return file_dict


if __name__ == '__main__':
    file_word_freq = get_file_word_freq('dataset.json')
    print(file_word_freq)
