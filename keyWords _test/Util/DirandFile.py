#encoding=utf-8
import os
from ProjectVar.Var import *
import time

def createDir(path,dirName):
    dirPath = os.path.join(path,dirName)
    if os.path.exists(dirPath):
        pass
    else:
        os.mkdir(dirPath)
