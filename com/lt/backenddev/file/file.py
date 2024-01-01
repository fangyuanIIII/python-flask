"""
文件编码
open(name,mode,encoding)打开函数
name   文件地址
mode  只读"r" 写入"w"  追加"a"
encoding  编码 "utf-8"
"""

fs = open(r"D:\a.txt","r",encoding="utf-8")

#读取全部文件  或者读取剩余没有读完的内容
# a = fs.read()

#读取10个字节的内容
# a1 = fs.read(10)

#读取全部行  封装到list列表中
# a2 = fs.readlines()
#读取一行内容
# a3 = fs.readline()

#循环读取文件内容
for line in fs:
    print(line)

#文件的关闭
fs.close()

"""
with open 语法块   会自动关闭close文件避免忘记
"""
with open(r"D:\a.txt","r",encoding="utf-8") as f:
    f.readlines()

"""
文件写入  
"""
#test.txt一个不存在的文件  会自动创建这个文件
fw = open(r"D:\test.txt","w",encoding="utf-8")
#写入到内存中
fw.write("Hello World!")
# 刷新   将内存中内容刷新到文件中
fw.flush()
#close方法自带flush方法 可以不写flush方法
fw.close()

#test.txt存在的文件    会将原先内容清空在写入数据
fw1 = open(r"D:\test.txt","w",encoding="utf-8")
#写入到内存中
fw1.write("你好")
# 刷新   将内存中内容刷新到文件中
fw1.flush()
fw1.close()

#追加文件内容   文件不存在会创建文件  \n换行符
fa = open(r"D:\test.txt","a",encoding="utf-8")
fa.write("\nasdadad")
fa.close()