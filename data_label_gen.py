import os
import random

def all_words_list(dir_path):
    """
    生成目录下的所有词语列表
    :param words_list: 词语文件的母文件夹
    :return: 所有词语的列表

    """
    all_words = []
    words_list = os.listdir(dir_path)
    for file_name in words_list:
        with open(f'{dir_path}/{file_name}') as f:
            if file_name == 'chi.txt':
                words = [part.strip() for part in f.readlines()]
                for i in range(100):
                    all_words.extend(words)
            else:
                words = [part.strip() for part in f.readlines()]
                all_words.extend(words)
        print(len(all_words))
        all_words.extend(words)


    return all_words


# 将序号与文字混合
def add_num_words(num_file, word_file, total):

    num_words_list = []
    with open(num_file) as f:
        num_list = [part.strip() for part in f.readlines()]

    with open(word_file) as f:
        chi_list = [part.strip() for part in f.readlines()]

    for i in range(total):
        index = random.randint(0, 1)
        num = random.choice(num_list)
        word = random.choice(chi_list)
        if index == 0:
            num_words_list.append(num+word)
        else:
            num_words_list.append(word+num)

    return num_words_list


def name_label(all_words):

    all_list = []
    for i in range(len(all_words)):
        all_list.append(all_words[i])
    return all_list


def label_txt(out_path, all_dict):

    with open(out_path, 'w') as f:
        for i in range(len(all_dict)):
            f.write(f'{all_dict[i]}\n')


def add_blank_label(num, all_list):

    for i in range(num):
        all_list.append('?')
    return all_list


if __name__ == '__main__':

    dir_path = './words'
    out_path = './data_set/train_word.txt'
    num_file = './words/add.txt'
    ref_file = './words/ref.txt'
    ref2_file = './words/ref2.txt'

    all_words = all_words_list(dir_path)
    print(len(all_words))
    # 21w+
    num_ref = add_num_words(num_file, ref_file, 100000)
    all_words.extend(num_ref)
    num_ref2 = add_num_words(num_file, ref2_file, 100000)
    all_words.extend(num_ref2)
    print(len(all_words))
    # 41w+
    all_words = add_blank_label(10000, all_words)
    print(f'last:{len(all_words)}')
    all_list = name_label(all_words)
    # print(all_dict)
    label_txt(out_path, all_list)



