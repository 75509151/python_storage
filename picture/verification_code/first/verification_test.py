# coding: utf-8
import unittest
import Image

import sys
from pytesseract import *
'''
三、一般思路

    验证码识别的一般思路为：

    1、图片降噪

    2、图片切割

    3、图像文本输出

3.1 图片降噪

所谓降噪就是把不需要的信息通通去除，比如背景，干扰线，干扰像素等等，只剩下需要识别的文字，让图片变成2进制点阵最好。
对于彩色背景的验证码：每个像素都可以放在一个5维的空间里，这5个维度分别是，X,Y,R,G,B，也就是像素的坐标和颜色，在计算机图形学中，有很多种色彩空间，最常用的比如RGB，印刷用的CYMK，还有比较少见的HSL或者HSV，每种色彩空间的维度都不一样，但是可以通过公式互相转换。在RGB空间中不好区分颜色，可以把色彩空间转换为HSV或HSL。色彩空间参见 http://baike.baidu.com/view/3427413.htm 

    验证码图片7039.jpg：

1、导入Image包，打开图片：
2、把彩色图像转化为灰度图像。RBG转化到HSI彩色空间，采用I分量：
3、二值化处理

二值化是图像分割的一种常用方法。在二值化图象的时候把大于某个临界灰度值的像素灰度设为灰度极大值，把小于这个值的像素灰度设为灰度极小值，从而实现二值化（一般设置为0-1）。根据阈值选取的不同，二值化的算法分为固定阈值和自适应阈值，这里选用比较简单的固定阈值。

把像素点大于阈值的设置,1，小于阈值的设置为0。生成一张查找表，再调用point()进行映射。
3.2 图片切割

识别验证码的重点和难点就在于能否成功分割字符，对于颜色相同又完全粘连的字符，比如google的验证码，目前是没法做到5%以上的识别率的。不过google的验证码基本上人类也只有30%的识别率。本文使用的验证码例子比较容易识别。可以不用切割，有关图片切割的方法参见这篇博客：http://www.cnblogs.com/apexchu/p/4231041.html


'''


def main():
    # 1
    im = Image.open("../../data/genimage.png")
    imgry = im.convert('L')
    imgry.show()

    # 3.2
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    out.show()
    print(image_to_string(out, config='-psm 7'))


if __name__ == '__main__':
    main()
