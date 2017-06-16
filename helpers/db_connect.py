import pymysql
from helpers import config
from helpers.funcs import create_file, append_to_file
import os


def connect():
    try:
        conn = pymysql.connect('localhost', 'root', 'root', 'imagesearch')
        c = conn.cursor()
    except Exception as e:
        err_file = os.path.join(config.ERROR_DIR, config.DATABASE_ERR_FILE)
        create_file(err_file)
        append_to_file(err_file, "Error: {}".format(e))
        conn, c = (None, None)
    return conn, c
