# -*- coding: utf-8 -*-
# @Time    : 20-2-13 ????5:03
# @Author  : wusaifei
# @FileName: Vision_data.py
# @Software: PyCharm

import pandas as pd
import seaborn as sns
import numpy as np
import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['figure.figsize'] = (10.0, 10.0)


# read data
ann_json = '/data/data_lyx/dota1_1024/trainval1024/DOTA_trainval1024.json'
with open(ann_json) as f:
    ann=json.load(f)

#import ipdb
#ipdb.set_trace()

#################################################################################################
# create catogory label dict
category_dic = dict([(i['id'],i['name']) for i in ann['categories']])
counts_label = dict([(i['name'],0) for i in ann['categories']])
for i in ann['annotations']:
    counts_label[category_dic[i['category_id']]]+=1

# annotate aspect ratio
box_w = []
box_h = []
box_wh = []
categorys_wh = [[] for j in range(15)] # dota has 15 classes.

#import ipdb
#ipdb.set_trace()
for a in ann['annotations']:
    if a['category_id'] != 0:
        if a['bbox'][3] == 0 or a['bbox'][2] == 0:  # had bug here: deviced by 0.
            continue
        box_w.append(round(a['bbox'][2],2))
        box_h.append(round(a['bbox'][3],2))
        wh = round(a['bbox'][2]/a['bbox'][3],0)
        if wh <1 :
            wh = round(a['bbox'][3]/a['bbox'][2],0)
        box_wh.append(wh)
        categorys_wh[a['category_id']-1].append(wh)


# aspect ratio of all labels
box_wh_unique = list(set(box_wh))
box_wh_count=[box_wh.count(i) for i in box_wh_unique]

# draw plot
wh_df = pd.DataFrame(box_wh_count,index=box_wh_unique,columns=['Aspect ratio numbers'])
wh_df.plot(kind='bar',color="#55aacc")
plt.show()