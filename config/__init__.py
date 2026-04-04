import pymysql
from .celery import celery

pymysql.version_info = (2, 2, 7, "final", 0)
pymysql.install_as_MySQLdb()
