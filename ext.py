## SqaushR Core V 1.0 ##
from os.path import splitext
def splitext_(path):
    if len(path.split('.')) > 2:
        return path.split('.')[0], '.'.join(path.split('.')[-2:])
    return splitext(path)
