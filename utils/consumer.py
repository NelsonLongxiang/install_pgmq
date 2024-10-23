#!/user/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2024/10/23 下午4:48
# @Author : 龙翔
# @File    :consumer.py
# @Software: PyCharm

import os
import sys
from typing import List

from common import postgres_dsn

# 将当前文件夹添加到环境变量
if os.path.basename(__file__) in ['run.py', 'main.py', '__main__.py']:
    if '.py' in __file__:
        sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    else:
        sys.path.append(os.path.abspath(__file__))
from pgmq_sqlalchemy import PGMQueue
from pgmq_sqlalchemy.schema import Message


pgmq = PGMQueue(dsn=postgres_dsn)

# read a single message
msg:Message = pgmq.read('my_queue',0)
print(msg)
#pgmq.archive('my_queue',msg.msg_id)

# pgmq.delete('my_queue',msg.msg_id)
# read a batch of messages
msgs:List[Message] = pgmq.read_batch('my_queue', 1)
print(len(msgs))
