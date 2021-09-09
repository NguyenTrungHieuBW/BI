# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 23:16:48 2021

@author: Admin
"""

import numpy as np
import pandas as pd
from googletrans import Translator
from googletrans import Translator, constants
import Dict as di
my_dict=di.dictionary()

movies_data = pd.read_csv("movies_metadata.csv")
del movies_data['homepage']
del movies_data['poster_path']
del movies_data['tagline']
del movies_data['id']
del movies_data['imdb_id']

movies_data.loc[movies_data['belongs_to_collection'].isna() == 1, 'belongs_to_collection']="No"
movies_data.loc[movies_data['video'].isna() == 1, 'belongs_to_collection']="No"
movies_data.loc[movies_data['spoken_languages'].isna() == 1, 'belongs_to_collection']="No data"
movies_data.loc[movies_data['original_language'].isna() == 1, 'original_language']="xx"

#if movies_data.loc[movies_data['original_language'].is_numeric():

header = list(movies_data.columns.values)
               

#print(type(movies_data["belongs_to_collection"][2]))

md=np.array(movies_data)
'''Xu ly mismatch'''
for i in(range(len(md))):
    if(md[i][0]=="TRUE" or md[i][0]=="FALSE" or md[i][0]=="NO DATA"):
        pass
    else:
        print(md[i][0])
        md[i][0]="NO DATA"


for i in(range(len(md))):
    deleted=0
    if(md[i][4].isnumeric()!=0):
        print(md[i][4])
        md = np.delete(md, [i], axis =0)
        deleted+=1
    if(i+deleted==len(md)-1):
        break
    
for i in(range(len(md))):
    deleted=0
    if(type(md[i][9])==float):
        print(md[i][9])
        md = np.delete(md, [i], axis =0)
        deleted+=1
    if(i+deleted==len(md)-1):
        break
    
for i in(range(len(md))):
    deleted=0
    if(type(md[i][8])==float):
        print(md[i][8])
        md = np.delete(md, [i], axis =0)
        deleted+=1
    if(i+deleted==len(md)-1):
        break


   
#a = md[2][1].split(sep="name': '")
#b = a[1].split(sep="', 'poster_path':")[0]

'''Sua lai cac cot'''
for i in(range(len(md))):
    a = md[i][8].split(sep="name': '")
    if(len(a)>1):
        md[i][8] = a[1].split(sep="', 'id':")[0]
      
for i in(range(len(md))):
    a = md[i][1].split(sep="name': '")
    if(len(a)>1):
        md[i][1] = a[1].split(sep="', 'poster_path':")[0]

#Product name
for i in(range(len(md))):
    a = md[i][9].split(sep="name': '")
    if(len(a)>1):
        md[i][9] = a[1].split(sep="'}")[0]

for i in(range(len(md))):
    md[i][4]=my_dict[md[i][4]]

for i in(range(len(md))):
    a = md[i][3].split(sep="}, {")
    md[i][3]=[]
    for j in(range(len(a))):
        b = a[j].split(sep="'name': '")
        if(len(b)>1):
            md[i][3]=np.append(md[i][3],b[1].split(sep="'")[0])
    
for i in(range(len(md))):
    a = md[i][13].split(sep="}, {")
    md[i][13]=[]
    for j in(range(len(a))):
        b = a[j].split(sep="iso_639_1': '")
        if(len(b)>1):
            md[i][13]=np.append(md[i][13],my_dict[b[1].split(sep="'")[0]])
#    if(len(a)>1):
#        md[i][3] = a[1].split(sep="'}")[0]

'''Luu file'''
df = pd.DataFrame(md,columns = [header[j] for j in range(19)])

df.to_csv(index=False)

compression_opts = dict(method='zip', archive_name='movies.csv')

df.to_csv('movies.zip', index=False,compression=compression_opts)
#    if(type(md[i][1]) is dict()):
#        list(dict.items())
#        md[i][1] = list(md.key('name'))
#        print(md[i][1].get('name'))
#    if(md[i][1]):
'''
for i in(range(len(md))):
    md[i][1].get('name')
    md[i][1] = list(md.key('name'))

for i in(range(len(md))):
    md[i][1].get('name')
    md[i][1] = list(md.key('name'))   
'''
#f = open("movies_metadata.csv","r")