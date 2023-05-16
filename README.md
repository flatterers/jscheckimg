# jscheckimg
以json中的键名为参照，查询文件夹内文件，并拷贝改名
支持各种文件类型

额外装个库 jsonpath 
pip install jsonpath

例如将A文件内的各种文件根据json文件中你所提取出的名称依次移动到另一个文件B中并改名,并输出同一名字下的不同文件名（更改过的），最后打印出excl。
