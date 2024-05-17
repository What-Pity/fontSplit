# 分割白纸上的汉字

自动分割白纸上的汉字，并将其转换为图片。作为[SDT](https://github.com/dailenson/SDT)的前处理步骤。

# 使用方法

1. `randomCharaterGenerate.py` 用于生成随机不重复汉字，并将其保存为txt文档。
2. 在白纸上手写汉字，将其保存为图片。
3. 修改`isolate.py`中的`image_path`和为保存图片的路径，运行，输出结果存储到`./output`文件夹中。
> 注意：修改闭运算核的大小可适配不同大小的汉字，字号越大，核的大小应该也越大