"""
Simple to rename pics extracked from the divine gate 图鉴 app
"""

import os
import re

def rename_pic(_path, _header):
    if not os.path.exists(_path):
        print(_path + ' can not be found.')
        return 

    file_list = os.listdir(_path)

    for file_name in file_list:
        header = re.search(_header, file_name)
        if header != None:
            os.rename(_path + "\\" + file_name, _path + "\\" + header.group() + ".png")


if __name__ == '__main__':
    rename_pic("D:\\tmp\\divine_charactor_4", r'^unit_[\d]{4}')