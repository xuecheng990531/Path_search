import os
import random


def updateFile(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)
def place(zi,mu):
    """查询子字符串在大字符串中的所有位置"""
    len1 = len(zi)
    pl = []
    if zi == mu:
        pl.append(0)
    else:
        for each in range(len(mu)-len1):
            if mu[each:each+len1] == zi:       # 找出与子字符串首字符相同的字符位置
                pl.append(each)
    return pl

def count_words(file_name):
    try:
        with open(file_name, encoding='utf8') as file_obj:
        #由于书名不是英文，要加上 encoding='utf8'
            contents = file_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file' + file_name + ' does not exist.'
        print(msg)
    else:
        words = contents.rstrip()
        num_words = len(words)
        return num_words

if __name__=='__main__':
    file='/Users/lixuecheng/Desktop/good/txt/network_final.txt'
    file_count=open(file)
    res=file_count.read()
    length=count_words(file)

import os, shutil,re

if __name__=='__main__':
    work_dir = '/Users/lixuecheng/Desktop/good/txt'
    new_dir = '/Users/lixuecheng/Desktop/good/txt/modified'
    for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            file = open(file_path,"r+",encoding="unicode_escape")
            newFile = open(new_dir+filename,"w",encoding="unicode_escape")
            for line in file.readlines():
                if(";1" in line):
                    # num = re.sub("\D", "", line)
                    # newNum = int(num)/3
                    # newNum = ("%.1f" % newNum)
                    # ori = line.split("\"")
                    line = line.replace(';1',';'+str(random.randint(1, 100)))
                    print(line)
                newFile.writelines(line)
            # print (filename)
            # newFile.close()
            # file.close()




