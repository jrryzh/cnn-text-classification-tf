# -*- coding:utf-8*-
import sys
import os
import os.path
import time


def MergeTxt(parentpath):
    print('开始处理文件')
    dir_list = [d for d in os.listdir(parentpath) if '.' not in d]
    for dir in dir_list:
        print('当前文件夹：%s' % dir)
        path = parentpath + '/' + dir
        for file_name in os.listdir(path):
            with open(path + '/' + file_name, 'r') as f:
                lines = [l.strip('\n') for l in f.readlines()]
            with open(path + '/' + file_name, 'w+') as f:
                for l in lines:
                    f.write(l)

    print('全部完成！')


def MergeTxt2(sourcePath, outPath):
    k = open(outPath, "w")
    txtList = os.listdir(sourcePath)
    txtList.sort()
    for txtPath in txtList:
        f = open(sourcePath + "/" + txtPath)
        k.write(f.read())
        k.write("\n")
    k.close()
    print("finished")


# if __name__ == '__main__':
#     parentpath = '/home/newdisk/zjy/datasets/PascalSentenceDataset/sentence'
#     MergeTxt(parentpath)

if __name__ == '__main__':
    parentpath = '/home/newdisk/zjy/datasets/PascalSentenceDataset/sentence'
    dirlist = [f for f in os.listdir(parentpath) if not f.startswith('.')]
    dirlist.remove('sentences_merge.py')
    dirlist.sort()

    for dir in dirlist:
        outfile = str(dir) + ".txt"
        filepath = parentpath + "/"
        MergeTxt2(sourcePath=parentpath + "/" + dir, outPath= "/home/newdisk/zjy/datasets/PascalSentenceDataset/merged_sentence/" + outfile)
