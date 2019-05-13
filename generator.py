from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import glob
import numpy as np
# from alpha_gen import to_dictionary
import os
import cv2


'''
1. 从文字库随机选择10个字符
2. 生成图片
3. 随机使用函数
'''
def noisy(image):

   # if noise_typ == "gauss":
   #    row, col, ch = image.shape
   #    mean = 0
   #    var = 0.5
   #    sigma = var**2
   #    gauss = np.random.normal(mean, sigma, (row, col, ch))
   #    gauss = gauss.reshape(row, col, ch)
   #    noisy = image + gauss
   #    return noisy

   effect = random.uniform(0.3, 0.7)
   row, col, ch = image.shape
   noise = np.zeros(image.shape)
   for _ in range(int(effect*row*col)):
       r_index = random.randint(0, row-1)
       c_index = random.randint(0, col-1)


def salt(img, n):
    # 循环添加n个椒盐
    for k in range(n):
        # 随机选择椒盐的坐标
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        # 如果是灰度图
        if img.ndim == 2:
            img[j,i] = 255
        # 如果是RBG图片
        elif img.ndim == 3:
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
    return img

# 从文字库中随机选择[2, 10]个字符
def sto_choice_from_info_str(rand_word_num):
    start = random.randint(0, len(info_str)-rand_word_num-1)
    end = start + rand_word_num
    random_word = info_str[start:end]

    return random_word

def random_word_color():
    font_color_choice = [[54,54,54],[54,54,54],[105,105,105]]
    font_color = random.choice(font_color_choice)

    noise = np.array([random.randint(0,10),random.randint(0,10),random.randint(0,10)])
    font_color = (np.array(font_color) + noise).tolist()

    #print('font_color：',font_color)

    return tuple(font_color)


# 生成一张图片
def create_an_image(bground_path, width, height):

    noise_choice = ['blank', 'noise']
    rand_dir = random.choice(noise_choice)
    bground_list = os.listdir(f'{bground_path}/{rand_dir}')
    bground_choice = random.choice(bground_list)
    bground = Image.open(f'{bground_path}/{rand_dir}/{bground_choice}')
    # print(f'{bground_path}/{rand_dir}/{bground_choice}')
    # print(width, height)
    # print(f'the choise is {bground.size[0]-width} {bground.size[1]-height}')
    if bground.size[0]-width or bground.size[1]-height <= 0:
        x, y = random.randint(0, 0), random.randint(0, 0)
    else:
        x, y = random.randint(0, bground.size[0]-width), random.randint(0, bground.size[1]-height)

    # print(f'the size of image: {bground.size[0]} {bground.size[1]}')
    # print(f'{x + width} {y + height}')
    bground = bground.crop((x, y, x+width, y+height))

    return bground

# 选取作用函数
def random_choice_in_process_func():
    pass

# 模糊函数
def darken_func(image):
    #.SMOOTH
    #.SMOOTH_MORE
    #.GaussianBlur(radius=2 or 1)
    # .MedianFilter(size=3)
    # 随机选取模糊参数
    filter_ = random.choice(
                            [ImageFilter.SMOOTH,
                            ImageFilter.SMOOTH_MORE,
                            ImageFilter.GaussianBlur(radius=1.3)]
                            )
    image = image.filter(filter_)
    #image = img.resize((290,32))

    return image


# 旋转函数
def rotate_func():
    pass


# 噪声函数
def random_noise_func():
    pass


# 字体拉伸函数
def stretching_func():
    pass


# 随机选取文字贴合起始的坐标, 根据背景的尺寸和字体的大小选择
def random_x_y(bground_size, font_size, len_word):

    width, height = bground_size
    # 为防止文字溢出图片，x，y要预留宽高
    x = random.randint(0, width-font_size * len_word)
    y = random.randint(0, int((height-font_size)/2))

    return x, y


def random_font_size():

    font_size = random.randint(60, 120)
    return font_size


def random_font(font_path):
    font_list = os.listdir(font_path)
    random_font = random.choice(font_list)

    return font_path + random_font


def main(save_path, word, num):

    # 计算字符长度
    word_len = len(word)

    # 随机选取字体大小
    font_size = random_font_size()

    # 生成一张背景图片，已经剪裁好
    img_h_list = [font_size+int(i*font_size/2) for i in range(1, 5)]
    img_w_list = [font_size*(word_len+i) for i in range(1, 4)]

    raw_image = create_an_image('./background', random.choice(img_w_list), random.choice(img_h_list))

    # 随机选取字体
    font_name = random_font('./font/')
    font_color = (0, 0, 0)

    # 随机选取文字贴合的坐标 x,y
    draw_x, draw_y = random_x_y(raw_image.size, font_size, word_len)

    # 将文本贴到背景图片
    font = ImageFont.truetype(font_name, font_size)
    draw = ImageDraw.Draw(raw_image)
    if word == '?':
        draw.text((draw_x, draw_y), ' ', fill=font_color, font=font)
        print(f'{save_path}{word}_{str(num)}.jpg')
    else:
        draw.text((draw_x, draw_y), word, fill=font_color, font=font)

    # 随机选取作用函数和数量作用于图片
    #random_choice_in_process_func()
    # raw_image = darken_func(raw_image)
    #raw_image = raw_image.rotate(0.3)
    # 添加高斯白噪声
    # raw_image = noisy("gauss", raw_image)

    # 保存文本信息和对应图片名称
    #with open(save_path[:-1]+'.txt', 'a+', encoding='utf-8') as file:
    # file.write(str(num)+ '.png ' + random_word + '\n')
    # a = f'{save_path}{random_word}_{str(num)}.png'

    raw_image.save(f'{save_path}{word}_{str(num)}.jpg')
    img = cv2.imread(f'{save_path}{word}_{str(num)}.jpg')
    # img = noisy(img)
    [w, h] = img.shape[:2]
    effect = random.uniform(0, 0.01)
    n = int(w*h*effect)
    # salt(img, n)
    # if random.randint(0, 1):
    # if 1:
    #     img = cv2.dilate(img, (3, 3))
    img = cv2.GaussianBlur(img, (3, 3), 1)
    # print(img.shape)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY)[1]
    salt(img, n)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    # print(img.shape)
    cv2.imwrite(f'{save_path}{word}_{str(num)}.jpg', img)


if __name__ == '__main__':

    with open('data_set/train_word.txt', 'r', encoding='utf-8') as file:
        info_list = [part.strip() for part in file.readlines()]
        # info_str = ''.join(info_list)

    # 所有数据集数量 98w+
    total = len(info_list)
    print(total)
    # 从98w+中选取10w作为验证
    arr_num = np.random.permutation(total)
    arr_list = arr_num.tolist()
    # print(arr_list)

    val_set = []
    train_set = []
    for i in range(100000):
        val_set.append(info_list[arr_list[i]])

    for j in range(100000, total):
        train_set.append(info_list[arr_list[j]])

    # 训练集生成
    print(f'{len(train_set)} will be generated...')
    for num in range(0, len(train_set)):
        word = train_set[num]
        main('./data_set/train_set/', word, num)
        if num % 1000 == 0:
            print('[%d/%d]' % (num, len(train_set)))
    print('Finish')

    验证集生成
    print(f'{len(val_set)} will be generated...')
    for num in range(0, len(val_set)):
        word = val_set[num]
        main('./data_set/val_set/', word, num)
        if num % 1000 == 0:
            print('[%d/%d]' % (num, len(val_set)))
    print('Finish')




