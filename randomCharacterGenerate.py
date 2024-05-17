import random

# 定义生成汉字的数量
num_characters = 100

# 汉字的Unicode编码范围
start_unicode = 0x4E00  # 汉字的起始Unicode编码
end_unicode = 0x9FFF   # 汉字的结束Unicode编码

# 生成一个包含所有可能汉字的列表
all_characters = [chr(code) for code in range(start_unicode, end_unicode + 1)]

# 从所有汉字中随机选择不重复的汉字
random_characters = random.sample(all_characters, num_characters)

# 定义要输出的文件名
output_file = 'random_characters.txt'

# 打开文件，准备写入
with open(output_file, 'w', encoding='utf-8') as f:
    # 将每个汉字写入文件，并在每个汉字后添加一个换行符
    for character in random_characters:
        f.write(character + ' ')

print(f"汉字已写入文件：{output_file}")
