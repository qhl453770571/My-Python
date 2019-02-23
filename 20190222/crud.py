-import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='nsd1809',
    charset='utf8'
)
cursor = conn.cursor()  # 创建游标，类似于文件对象，用它来执行SQL语句

# insert_dep1 = 'INSERT INTO department(dep_id,dep_name) VALUES (%s,%s)'
# cursor.execute(insert_dep1,(1,'人事部'))
# cursor.executemany(insert_dep1,[(4,'测试部'),(5,'行政部')])

# insert_emp1 = 'insert into employees values(%s,%s,%s,%s,%s,%s)'
# cursor.executemany(insert_emp1,
#                    [(1,'qiaoxin','girl','2016-1-10','qiaoxin@qq.com',2),
#                     (2,'linlin','girl','1991-1-10','lin@qq.com',3)])

# query_dep1='select * from department'
# cursor.execute(query_dep1)

# result1=cursor.fetchone()
# print(result1)
# print('*'*30)
#
# result2=cursor.fetchmany(2)
# print(result2)
# print('*'*30)
#
# result3=cursor.fetchall()
# print(result3)
# print('*'*30)

# cursor.scroll(2,mode='absolute')
# result4=cursor.fetchone()
# print(result4)
#
# cursor.scroll(1)
# result5=cursor.fetchone()
# print(result5)

# update_dep1='update department set dep_name=%s where dep_name=%s'
# cursor.execute(update_dep1,('运维开发部','运维部'))

delete_dep1='delete from department where dep_id=%s'
cursor.execute(delete_dep1,(1,))

conn.commit()
cursor.close()
conn.close()
