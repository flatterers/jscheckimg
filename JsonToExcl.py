import os
import jsonpath
import json
import pandas as pd
import numpy as np

# 根据键名取值
def get_json_value(json_data,key_name):

    key_value = jsonpath.jsonpath(json_data, '$..{key_name}'.format(key_name=key_name))
    #key的值不为空字符串或者为empty（用例中空固定写为empty）返回对应值，否则返回empty
   
    return key_value

# 以名字查找文件夹内对应的文件，并拷贝到另一个文件 path1为查找的文件夹路径，path2为拷贝到的文件夹路径，name1为查找的名称
def main1(path1,path2,name1):
    originalname = name1
    replacename = name1
    files = os.listdir(path1)  # 得到文件夹下的所有文件名称
    for file in files: #遍历文件夹
        if os.path.isdir(path1 + '\\' + file):
            i=0
            main1(path1 + '\\' + file)
        else:
            files2 = os.listdir(path1 + '\\')
            i=1
            for file1 in files2:
                if originalname in file1:
                    type=os.path.splitext(file1)[1]
                    #用‘’替换掉 X变量 
                    n1 = str(path1 + '\\' + str(file1))
                    n2 = str(path2 + '\\' + file1.replace(str(file1),replacename+str(i)+str(type)))
                    i=i+1
                    # print(n1,n2,i)
                    os.rename(n1,n2)

filePath1 = '.\img\乌畴溪新村'
filePath2 = '.\img_change\乌畴溪新村'


# 以键名获得数值
json_text=r'.\json\乌畴溪新村.geojson'
with open(json_text,encoding='utf8') as f:
    content = json.load(f)
names=get_json_value(content, "名称")
# names=np.unique(names)   # 清除重复的 这个会重新排序

# 以名称为参照拷贝
for name in names:
    main1(filePath1,filePath2,name)


# 获取拷贝后的文件夹内的文件名，无后缀
img_name=[]
img_type=[]
imgs = os.listdir(filePath2)
for img in imgs:
    type=os.path.splitext(filePath2+'\\'+img)[1]
    img_type.append(type)
    index = img.rfind('.')
    img = img[:index]
    img_name.append(img)
# print(img_type)
# print(img_name)

    

# 将原名称的数组进行重构以便于后续数据插入
arry_num = [[i] for i in names]
i=0
for item1 in names:
    j=0
    for item2 in img_name:
        if item1 in item2 and len(item1+'1')==len(item2):    # 这里需要添加对长度的判断
                file_name=item2+str(img_type[j])
                # print(item2)
                # print(img_type[j])
                arry_num[i].append((file_name))
        j=j+1
    i=i+1


#将数据导出到excl
data = pd.DataFrame(arry_num)

writer = pd.ExcelWriter('.\excl\\num.xlsx')		# 写入Excel文件
data.to_excel(writer, 'page_1', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()


