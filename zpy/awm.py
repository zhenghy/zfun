import os
import re
import sys
from time import localtime, strftime

import pymysql


def astr(strobj):
    """
    :param strobj:
    :return a str type value:
    """
    try:
        return str(strobj)
    except:
        return strobj


def anum(numobj):
    """
    :param intobj:
    :return a num type value:
    """
    try:
        return float(numobj)
    except:
        return numobj


def nowf(format='t'):
    """
    :param format: a time format marker:
    :return a str value:
    """
    if format == 's':
        # serial
        format = '%Y%m%d%H%M%S'
    if format == 't':
        # time
        format = '%Y-%m-%d %H:%M:%S'
    if format == 'd':
        # date
        format = '%Y-%m-%d'
    return strftime(format, localtime())


def amkdir(dir_name):
    # curdir=os.path.split(os.path.abspath(sys.argv[0]))[0]
    curdir = os.getcwd()
    credir = os.path.join(curdir, dir_name)
    if not os.path.exists(credir):
        os.mkdir(dir_name)
    return credir


def script(fpath, s):
    """
    Create a executable file include command s.
    :param fpath: file path (include name.)
    :param s: file content.
    :param c: execute command.
    :return: fpath.
    """
    import os
    fpath = os.path.abspath(fpath)
    with open(fpath, 'w') as f:
        f.write(s + '\n')
    os.system('chmod +x ' + fpath)
    return fpath


class MYSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if self.db:
            try:
                self.conn = pymysql.connect(host=self.host,
                                            user=self.user,
                                            password=self.pwd,
                                            database=self.db)
            except:
                exit("Don't a MySQL or MSSQL database.")
        else:
            exit("No database.")
        cur = self.conn.cursor()
        if not cur:
            exit("Error connect")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        try:
            cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        self.conn.close()

    def UpdateInsert(self, table, column, value):
        """
        table : 'table name'
        column: ['c1','c2','c3']
        value : ["(1,'2','a')","(2,'3','b')"]
        NOTES : `ON DUPLICATE KEY UPDATE`, UNIQUE INDEX is necessary.
        """
        sql_col = [f'`{i}`' for i in column]
        sql_val = ',\n'.join(value)
        sql = f"""
        INSERT INTO {table}({','.join([ _ for _ in sql_col])}) VALUE 
        {sql_val}
        ON DUPLICATE KEY UPDATE {','.join([_+'=VALUES('+_+')' for _ in sql_col])}
        """
        sql = re.sub(r'\s*\n\s*', '\n', sql) ##tidy
        self.ExecNonQuery(sql)
        return sql


def test():
    print(nowf('s'))
    print(nowf('t'))
    print(nowf('d'))
    print(astr('110'))
    print(astr(110))
    print(anum(110))
    print(anum('110'))


if __name__ == "__main__":
    test()
