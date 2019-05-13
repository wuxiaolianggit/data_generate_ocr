


if __name__ == '__main__':

    label_file = open('./data_set/train_set.txt', 'r')
    while 1:
        line = label_file.readline()
        print(line.strip().split('\t'))
        if not line:
            break