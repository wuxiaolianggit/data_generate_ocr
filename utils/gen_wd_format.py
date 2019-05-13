# 将分隔的字，组织成每行一个词或字的形式

split_para = ' '
file_path = '../words/chi.txt'
out_path = '../words/chi.txt'

if __name__ == '__main__':
    with open(file_path, 'r') as f:
        for line in f.readlines():
            str_words = ''.join(line)
            list_words = str_words.split(split_para)

    with open(out_path, 'w') as f:
        for word in list_words:
            f.write(f'{word}\n')


