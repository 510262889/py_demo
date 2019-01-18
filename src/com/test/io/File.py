import os

import numpy as np

def read(filePath):
    if not filePath or (not os.path.exists(filePath)):
        raise IOError("读取文件不存在!")
    file = None
    try:
        file = open(filePath, "r")
        content = file.read()
    finally:
        if file:
            file.close()
    return content


def loadDataSet(filename):
    """
        读取数据
        Args:
            filename: 文件名

        Returns:
            X: 训练样本集矩阵
            y: 标签集矩阵
    """
    numFeat = len(open(filename).readline().split('\t')) - 1
    X = []
    y = []
    file = open(filename)
    for line in file.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        X.append(lineArr)
        y.append(float(curLine[-1]))
    return np.mat(X), np.mat(y).T
