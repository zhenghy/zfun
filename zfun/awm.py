import re
from time import localtime, strftime

import pymysql


def nowf(former='t'):
    """
    format now time to a fix form.
    :param former: a datetime format marker:
        t -- time -- '2099-01-01 00:00:00' (default)
        s -- serial -- '20990101000000'
        d -- date -- '2099-01-01'
        other -- '%Y%m%d%H%M%S...'
    :return: a str value.
    """
    person = {'s': '%Y%m%d%H%M%S',
              't': '%Y-%m-%d %H:%M:%S',
              'd': '%Y-%m-%d'}
    # noinspection PyBroadException
    try:
        former = person.get(former, former)
        return strftime(former, localtime())
    except Exception as e:
        print('a flaw/blemish datetime former')


def script(fpath, s):
    """
    Create a executable file include command s.
    :param fpath: file path (include name.)
    :param s: file content.
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
            # noinspection PyBroadException
            try:
                self.conn = pymysql.connect(host=self.host,
                                            user=self.user,
                                            password=self.pwd,
                                            database=self.db,
                                            use_unicode=True,
                                            charset='utf8'
                                            )
            except Exception as e:
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
        res = cur.fetchall()
        self.conn.close()
        return res

    def ExecNonQuery(self, sql):
        """
        Exec a mysql query with insert/update/delete
        :param sql: a list of sql query
        :return: 0 for failed , 1 for successed.
        """
        cur = self.__GetConnect()
        ok = 0
        # noinspection PyBroadException
        try:
            [cur.execute(i) for i in sql]
            self.conn.commit()
            ok = 1
        except Exception as e:
            self.conn.rollback()
        self.conn.close()
        return ok

    @staticmethod
    def update_insert_sql(table, column, value):
        """
        table : 'table name'
        column: ['c1','c2','c3']
        value : ["(1,'2','a')","(2,'3','b')"]
        NOTES : `ON DUPLICATE KEY UPDATE`, UNIQUE INDEX is necessary.
        """
        sql_col = [f'`{i}`' for i in column]
        sql_val = ',\n'.join(value)
        sql = f"""
        INSERT INTO {table}({','.join([_ for _ in sql_col])}) VALUE 
        {sql_val}
        ON DUPLICATE KEY UPDATE {','.join([_ + '=VALUES(' + _ + ')' for _ in sql_col])}
        """
        sql = re.sub(r'\s*\n\s*', '\n', sql)  ##tidy
        return sql


def test():
    print(nowf('s'))
    print(nowf('t'))
    print(nowf('d'))


if __name__ == "__main__":
    test()