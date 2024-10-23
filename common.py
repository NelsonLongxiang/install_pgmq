#!/user/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2024/10/23 下午11:30
# @Author : 龙翔
# @File    :common.py
# @Software: PyCharm

import os
import sys

# 将当前文件夹添加到环境变量
if os.path.basename(__file__) in ['run.py', 'main.py', '__main__.py']:
    if '.py' in __file__:
        sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    else:
        sys.path.append(os.path.abspath(__file__))

postgres_dsn = 'postgresql://postgres:123456@192.168.29.129:5432/postgres'