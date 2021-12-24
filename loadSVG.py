# -*- coding: UTF-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
import fontforge
import json
jsonPath='./txt9169.json'

rootdir = '/home/wjj/PythonProject/flask-main/font-dataset/'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    import uniout
    import re

    alphas = re.findall(r"\D+", list[i])
    digtal = re.findall(r"\d+", list[i])
    path = os.path.join(rootdir,list[i])
    print(path)
    if os.path.isfile(path):
       font=fontforge.open(path)               #Open a font
       font.em = 256
       filePath='./LYJ300-1223/'
       if not os.path.exists(filePath):
             os.mkdir(filePath)


       cjk = json.load(open(jsonPath))
       CN_CHARSET = cjk["gbk"]

       count = 0
       sample_count = 62  # 生成几个字


       for c in CN_CHARSET:
           if count <= sample_count:
               count += 1
               try:
                   pen = font[ord(c)]  # 获取字形 unicode 编码 包含此字形的字体
                   print(alphas[0])
                   print(digtal[-1])
                   pen.export('./LYJ300-1223/' + str(count) + alphas[0] + '_' + digtal[-1] + '.png', 255)
               except:
                   print("None")