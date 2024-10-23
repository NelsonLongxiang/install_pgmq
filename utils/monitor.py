#!/user/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2024/10/23 下午4:48
# @Author : 龙翔
# @File    :monitor.py
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
from pgmq_sqlalchemy import PGMQueue
from pgmq_sqlalchemy.schema import QueueMetrics

pgmq = PGMQueue(dsn=postgres_dsn)

# get queue metrics
metrics: QueueMetrics = pgmq.metrics('my_queue')
print(metrics.queue_length)
print(metrics.total_messages)
