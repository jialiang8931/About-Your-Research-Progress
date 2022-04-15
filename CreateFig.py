#!/usr/bin/env python
# coding: utf-8


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import numpy as np


firstString = '早安你好'
listString = ['研究有進度嗎？', '今天天氣如何', '哪時候結婚',
          '學妹吃飯了嗎？', '活力的一天，讚', '平安喜樂',]


randomSeed = np.random.randint(0, len(listString))
img = Image.open("BaseFig.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# If a font is already installed in your system, you can 
# just give its name
font = ImageFont.truetype("simsun.ttc", 220) #arial SimHei
# draw.text((x, y),"Sample Text",(r,g,b))
# x, y is the top-left coordinate

secondString= listString[randomSeed]

offset = 200
draw.text((30, 1500-offset),"%6s" %firstString, (0,0,0),font=font)
draw.text((30, 1800-offset),"%6s" %secondString,(0,0,0),font=font)

img.save('sample-out.jpg')

