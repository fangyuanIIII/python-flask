"""
spark流式计算
pip install pyspark
pip install pyspark -i https://pypi.tuna.tsinghua.edu.cn/simple


数据输入 rdd弹性分布式式数据集

数据计算

数据输出
"""
import os
from pyspark import SparkContext, SparkConf
os.environ['PYSPARK_PYTHON'] = r'D:\Dev\DevEnvironment\PYTHON\Python312\python.exe' #写你自己的路径
# conf = SparkConf().setAppName("appname").setMaster(""local[*]")
# sc = SparkContext(conf=conf)
# print(sc.version)
#
# sc.stop()

"""
数据输入
"""
conf = SparkConf().setAppName("appname").setMaster("local[*]")
sc = SparkContext(conf=conf)

#parallelize  将python容器加载转为rdd
rdd1 = sc.parallelize([1,"ad",True])
print(rdd1.collect())
#textFile 读取文件转为rdd
textrdd = sc.textFile("D:/a.txt")
print(textrdd.collect())

"""
数据计算
"""
def func_(data):
    print(data)
    return data * 2

rdd2 = sc.parallelize([1,2,3,4,5,6])
#map算子  获取元素 rdd列表    处理数据返回rdd
rdd2_new = rdd2.map(func_)
print(rdd2_new.collect())
#flatMap  解除嵌套 取元素 rdd列表    处理数据返回rdd
rdd3 = sc.parallelize([[1,2,3,4],[2,4,5,6,8]])
rdd3_new = rdd3.flatMap()  #结果[1,2,3,4,2,4,5,6,8]
#
rdd4 = sc.parallelize([("男",12),("男",34),("女",6),("女",10)])
#reduceByKey聚合操作  求两个组之和 针对kv型
rdd4_new = rdd4.reduceByKey(lambda x, y: x + y) #结果[("男",46),("女",16)]

#reduce 聚合操作  前两个加的结果 再继续进行加另一个  a+b=result  result + b = result2  result2 + b = result3...
rdd9 = sc.parallelize([1,2,3,4,5,6])
rdd9_new = rdd4.reduce(lambda x, y: x + y)#结果 21

#小练 求聚合
rdd5 = sc.parallelize(["a","b","b","d","a","c"])
rdd5_new = rdd5.map(lambda x : (x,1))
rdd5_new_new  = rdd5_new.reduceByKey(lambda x, y: x + y) #结果[("a",2),("b",2),("c",1),("d",1)]

#filter  过滤出要保留的数据    得到true保留
rdd6 = sc.parallelize([1,2,3,4,5,6])
rdd6_new = rdd6.filter(lambda x: x%2==0) # 过滤出偶数  结果[2,4,6]

#distinct数据去重操作
rdd7 = sc.parallelize([1,2,1,4])
rdd7_new = rdd7.distinct() #结果[1,2,4]

#排序sortBy
#keyfunc  排序依据
# ascending  升序True还是降序False
# numPartitions
rdd8 = sc.parallelize([("asdsad","adas",3),("ad","sc",3),("asd","asdad",5)])
#                      keyfunc依据元组的第三个元素的数字
rdd8_new = rdd8.sortBy(keyfunc = lambda x:x[2],ascending=False,numPartitions=1)

#take算子 取出前几位的结果
rdd10 = sc.parallelize([1,2,3,4,5,6])
rdd10_new = rdd10.take(3) #结果[1,2,3]
#count算子计算rdd有多少元素
count_ = rdd10.count()

"""
数据输出
"""
rdd10.saveAsTextFile("D:/out")

