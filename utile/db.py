import pymysql
from dbutils.pooled_db import PooledDB
from pymysql import cursors
POOL =PooledDB(
    creator=pymysql, #使用链接数据库模版
    maxconnections=10,   #连接池允许的最大连接数
    mincached=2,         #初始化时，连接池中至少创建的空闲的链接
    maxcached=5,         #连接池中最多空闲的链接数量
    blocking=True,       #连接池中如果没有可用连接后，会阻塞等待
    setsession=[],        #开始会话前执行的命令列表
    ping=0,

    host='47.115.211.11', post=3306, user='root', password='root123', charset="utf-8", db='user'
)

def fetch_one(sql,param):
    # conn = pymysql.connect(host='127.0.0.1', post=3306, user='root', password='root123', charset="utf-8", db='dat20')
    conn = POOL.connection()
    cursor = conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql, param)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def fetch_all(sql,param):
    # conn = pymysql.connect(host='127.0.0.1', post=3306, user='root', password='root123', charset="utf-8", db='dat20')
    conn = POOL.connection()
    cursor = conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql, param)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result