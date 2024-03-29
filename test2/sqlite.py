# encoding=utf-8





def get_i_sql(table, dict):
    '''
    生成insert的sql语句
    @table，插入记录的表名
    @dict,插入的数据，字典
    '''
    sql = 'insert into %s set ' % table
    sql += dict_2_str(dict)
    return sql


def get_s_sql(table, keys, conditions, isdistinct=0):
    '''
        生成select的sql语句
    @table，查询记录的表名
    @key，需要查询的字段
    @conditions,插入的数据，字典
    @isdistinct,查询的数据是否不重复
    '''
    if isdistinct:
        sql = 'select distinct %s ' % ",".join(keys)
    else:
        sql = 'select  %s ' % ",".join(keys)
    sql += ' from %s ' % table
    if conditions:
        sql += ' where %s ' % dict_2_str_and(conditions)
    return sql


def get_u_sql(table, value, conditions):
    '''
        生成update的sql语句
    @table，查询记录的表名
    @value，dict,需要更新的字段
    @conditions,插入的数据，字典
    '''
    sql = 'update %s set ' % table
    sql += dict_2_str(value)
    if conditions:
        sql += ' where %s ' % dict_2_str_and(conditions)
    return sql


def get_d_sql(table, conditions):
    '''
        生成detele的sql语句
    @table，查询记录的表名

    @conditions,插入的数据，字典
    '''
    sql = 'delete from  %s  ' % table
    if conditions:
        sql += ' where %s ' % dict_2_str_and(conditions)
    return sql


def dict_2_str(dictin):
    '''
    将字典变成，key='value',key='value' 的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), safe(str(v)))
        tmplist.append(' ' + tmp + ' ')
    return ','.join(tmplist)


# def dict_2_str_and(dictin):
#     '''
#     将字典变成，key='value' and key='value'的形式
#     '''
#     tmplist = []
#     for k, v in dictin.items():
#         tmp = "%s='%s'" % (str(k), safe(str(v)))
#         tmplist.append(' ' + tmp + ' ')
#     return ' and '.join(tmplist)


#数据库连接类


class SqlConn():
    def __init__(self):
        self.conn = DBpool.pool.connection()
        self.cur = self.conn.cursor()

    def cur(self):
        return self.cur()

    def commit(self):
        self.conn.commit()

    def execute(self, sql, fetchone=0):
        self.cur.execute(sql)
        return self.cur.fetchone() if fetchone else self.cur.fetchall()

    def last_id(self, table):
        sql = 'SELECT LAST_INSERT_ID() from %s' % table
        return self.execute(sql, 1)[0]

    def close(self):
        self.cur.close()
        self.conn.close()
