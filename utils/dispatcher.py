#!/user/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2024/10/23 下午4:48
# @Author : 龙翔
# @File    :dispatcher.py.py
# @Software: PyCharm

import os
import sys

from common import postgres_dsn

# 将当前文件夹添加到环境变量
if os.path.basename(__file__) in ['run.py', 'main.py', '__main__.py']:
    if '.py' in __file__:
        sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    else:
        sys.path.append(os.path.abspath(__file__))
from typing import List
from pgmq_sqlalchemy import PGMQueue


pgmq = PGMQueue(dsn=postgres_dsn)
pgmq.create_queue('my_queue')

msg = {'key': 'value', 'key2': 'value2'}
msg_id:int = pgmq.send('my_queue', msg)

# could also send a list of messages
msg_ids:List[int] = pgmq.send_batch('my_queue', [msg, msg])
print(msg_ids)