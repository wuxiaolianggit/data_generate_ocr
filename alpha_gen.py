import os

# words文件夹中的所有文件中的文字 剔除重复的 方便后续编码
# delete duplicate words of all files in words directory,
# and create a txt


dir_path = './words'
out_path = './alpha.txt'


# 将路径下的所有文件内容，剔除相同的字后，返回字典
def to_alpha(words, out_path):

	info_list = [part.strip() for part in words]
	string = ''.join(info_list)
	setting = set(string)
	# print(len(setting))
	with open(out_path, 'w') as file:
		string = ''.join(setting)
		file.write(string)
		# 添加?作为图片无文字标示
		file.write('?')


if __name__ == '__main__':

	words_dir = os.listdir(dir_path)
	# words_dir = ['ref.txt', 'ref2.txt']
	all_words = []
	for file in words_dir:
		with open(f'{dir_path}/{file}', 'r') as f:
			for part in f.readlines():
				all_words.append(part)

	to_alpha(all_words, out_path)





