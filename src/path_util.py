# coding: utf8

import os


def get_abs_dir_from_file_path(file_path):
    '''
    @brief 给定文件路径，获取文件所在目录的绝对路径
    '''
    path = os.path.dirname(file_path)
    path = os.path.abspath(path)
    return path
