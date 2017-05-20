import pymysql

def connect():
    try:
        conn = pymysql.connect('localhost', 'root', 'root',
                               'imagesearch')
        c = conn.cursor()
    except:
        conn, c = (None, None)
    return conn, c
