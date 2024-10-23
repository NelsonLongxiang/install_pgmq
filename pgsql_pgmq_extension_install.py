#!/user/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2024/10/23 下午11:03
# @Author : 龙翔
# @File    :pgsql_pgmq_extension_install.py
# @Software: PyCharm

import os
import sys
import psycopg2

from common import postgres_dsn

# 将当前文件夹添加到环境变量
if os.path.basename(__file__) in ['run.py', 'main.py', '__main__.py']:
    if '.py' in __file__:
        sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    else:
        sys.path.append(os.path.abspath(__file__))

conn = psycopg2.connect(dsn=postgres_dsn)
cursor = conn.cursor()
init_pgmq = '''
-- SCHEMA: pgmq

-- DROP SCHEMA IF EXISTS pgmq ;

CREATE SCHEMA IF NOT EXISTS pgmq
    AUTHORIZATION postgres;

GRANT USAGE ON SCHEMA pgmq TO pg_monitor;

GRANT ALL ON SCHEMA pgmq TO postgres;

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA pgmq
GRANT SELECT ON TABLES TO pg_monitor;

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA pgmq
GRANT SELECT ON SEQUENCES TO pg_monitor;
'''
install_pgmq = '''
-- Extension: pgmq

-- DROP EXTENSION pgmq;

CREATE EXTENSION IF NOT EXISTS pgmq
    SCHEMA pgmq
    VERSION "1.5.0";
'''
cursor.execute(init_pgmq)
conn.commit()
cursor.execute(install_pgmq)
conn.commit()
