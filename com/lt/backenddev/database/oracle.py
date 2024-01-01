"""
oracle数据库

oracle
python3.6或更高版本
pip install cx_Oracle --upgrade
"""

import cx_Oracle as Oracle

class OracleDatabase:
    def __init__(self):
        self.connection = self.connect_db("dev","123456",
                                          "localhost",1521,
                                          "orcl")
        self.cursor = self.connection.cursor()

    def connect_db(self,user :str,password :str,ip :str,port :int,service_name :str) -> Oracle:
        """定义连接"""
        # user = 'dev'
        # password = '123456'
        # host = 'localhost:1521'
        # service_name = 'orcl'
        conn_str = f"{user}/{password}@{ip}:{port}/{service_name}"
        try:
            connect = Oracle.connect(conn_str)
        except:
            print("连接错误")
        finally: return connect
        return connect

    def query_all(self, sql):
        """查询所有记录"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def query_one(self, sql):
        """查询单条记录
        查询第一条记录"""
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def query_by(self, sql, params):
        """根据条件查询记录"""
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def insert(self, sql, params):
        """插入数据"""
        self.cursor.execute(sql, params)
        self.connection.commit()
        print('[提示]：执行成功！')

    def update(self, sql, params):
        """修改数据"""
        self.cursor.execute(sql, params)
        self.connection.commit()
        print('[提示]: 修改完成！')

    def delete(self,sql, params):
        """根据条件，删除表数据"""
        self.cursor.execute(sql, params)
        self.connection.commit()
        print(f'[提示]: 删除成功，条件：{params}')

    def truncate(self, table_name):
        """清空表数据"""
        sql = f'truncate table {table_name}'
        self.cursor.execute(sql)
        self.connection.commit()
        print(f'[提示]: 清空表 {table_name} 成功')

    def procedure(self, params):
        """存储过程"""
        sql = "begin pkg_test.pro_test(:i_id, :i_name, :i_code); end;"
        self.cursor.execute(sql, params)
        self.connection.commit()
        print(f'[提示]: 调用存储过程成功，参数：{params}')
        """
        pkg head：
            create or replace package pkg_test is
            procedure pro_test(i_id in number,
                          i_name  in varchar2,
                          i_code  in varchar2);
            end pkg_test;
        
        pkg body：
            create or replace package body pkg_test is
    
            procedure pro_test(i_id in number,
                          i_name  in varchar2,
                          i_code    in varchar2) is
            begin
            execute immediate 'insert into ORDERS(id, name, code) values(:b1, :b2, :b3)'
             using i_id, i_name, i_code;
       
            commit;
            end pro_test;
            end pkg_test;
        """

oracle = OracleDatabase()
connect = oracle.connection

# cursor.execute('select * from ORDERS')
# print(cursor.fetchall())
print(oracle.query_all('select * from ORDERS'))
print(oracle.query_one('select * from ORDERS'))
print(oracle.query_by('select * from ORDERS where id=:id',
                      {"id":"92ffd585-385b-458f-be54-87839d6e0305"}))