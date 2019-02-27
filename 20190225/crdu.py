
from dbconn import Departments,Employees,Session

# hr=Departments(dep_name='人事部')
# ops=Departments(dep_name='运维部')
# dev=Departments(dep_name='开发部')
# qa=Departments(dep_name='测试部')
# finance=Departments(dep_name='财务部')
# xz=Departments(dep_name='行政部')

#
# p1=Employees(
#     emp_name='qiaoxin',
#     gender='女',
#     birth_date='2016-2-27',
#     email='qiao@qq.com',
#     dep_id=1
# )
#
# p2=Employees(
#     emp_name='linlin',
#     gender='女',
#     birth_date='1988-2-27',
#     email='lin@qq.com',
#     dep_id=2
# )
#
# p3=Employees(
#     emp_name='qihl',
#     gender='男',
#     birth_date='1985-2-27',
#     email='qihl@qq.com',
#     dep_id=3
# )
#
# p4=Employees(
#     emp_name='qiqiaoxin',
#     gender='女',
#     birth_date='2016-2-27',
#     email='qiaoxin@qq.com',
#     dep_id=4
# )
#
# p5=Employees(
#     emp_name='haijun',
#     gender='男',
#     birth_date='1992-2-27',
#     email='haijunqihl@qq.com',
#     dep_id=5
# )
#
# p6=Employees(
#     emp_name='haijun2',
#     gender='男',
#     birth_date='1992-2-27',
#     email='haijunqihl@qq.com',
#     dep_id=8
# )
#
# p7=Employees(
#     emp_name='haile',
#     gender='男',
#     birth_date='1985-2-27',
#     email='qihl@qq.com',
#     dep_id=8
# )

# gyh = Employees(
#     emp_name='耿宇航',
#     gender='男',
#     birth_date='1993-8-23',
#     email='gyh@qq.com',
#     dep_id=2
# )
# zjy = Employees(
#     emp_name='张钧溢',
#     gender='男',
#     birth_date='1990-10-15',
#     email='zjy@163.com',
#     dep_id=2
# )
# jp = Employees(
#     emp_name='蒋鹏',
#     gender='男',
#     birth_date='1995-3-23',
#     email='jp@qq.com',
#     dep_id=3
# )
# ljj = Employees(
#     emp_name='李杰君',
#     gender='男',
#     birth_date='1995-4-18',
#     email='ljj@126.com',
#     dep_id=3
# )
# ghn = Employees(
#     emp_name='郭浩南',
#     gender='男',
#     birth_date='1992-2-5',
#     email='ghn@qq.com',
#     dep_id=2
# )
# wyf = Employees(
#     emp_name='王宇峰',
#     gender='男',
#     birth_date='1994-12-9',
#     email='wyf@qq.com',
#     dep_id=4
# )
# cl = Employees(
#     emp_name='陈磊',
#     gender='男',
#     birth_date='1994-11-2',
#     email='cl@qq.com',
#     dep_id=2
# )
# xkn = Employees(
#     emp_name='徐康宁',
#     gender='男',
#     birth_date='1994-9-12',
#     email='xkn@qq.com',
#     dep_id=2
# )
# ytt = Employees(
#     emp_name='余婷婷',
#     gender='女',
#     birth_date='1996-5-18',
#     email='ytt@qq.com',
#     dep_id=3
# )


session=Session()
# session.add_all([gyh, zjy, jp, ljj, ghn, wyf, cl, xkn, ytt])

# session.add_all([hr,ops,dev,qa,finance,xz])
# session.add_all([p1,p2,p3,p4,p5,p6,p7])
#
# query1 = session.query(Departments)
# print(query1)  # query1只是一个SQL查询语句
# print(query1.all())  # 返回的是Departments所有实例组成的列表
# for dep in query1:   # 取出查询结果中的每一个实例
#     print(dep)
# for dep in query1:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))  # 打印实例的属性
# query2=session.query(Departments).order_by(Departments.dep_id)
# print(query2)
# for i in query2:
#     print('%s:%s' % (dep.dep_id,dep.dep_name))


# query3=session.query(Employees.emp_name,Employees.email)
# print(query3)
# print('*'*20)
# print(query3.all())
# print('*'*20)
# for name,email in query3:
#     print('%s:%s' % (name,email))
# print('*'*20)
#
# query4=session.query(Departments.dep_name.label('部'))
# print(query4)
# for dep in query4:
#     print(dep.部)

# query5=session.query(Departments).order_by(Departments.dep_id)
# dep=query5[0]
# print(dep)
# print('*'*20)
# print('%s:%s' % (dep.dep_id,dep.dep_name))
# qset=query5[1:3]
# print(qset)
# print('*'*20)
# for dep in qset:
#     print('%s:%s' % (dep.dep_id,dep.dep_name))

# query6=session.query(Employees).filter(Employees.dep_id==3)
# print(query6)
# for emp in query6:
#     print('%s:%s' % (emp.dep_id,emp.emp_name))

# query7=session.query(Employees).filter(Employees.dep_id==2).filter(Employees.email.like('%@qq.com'))
# print(query7.all())
# for emp in query7:
#     print('%s:%s' % (emp.emp_name,emp.email))

# query10=session.query(Departments).filter(~Departments.dep_id.in_([1,3]))
# print(query10)
# for dep in query10:
#     print('%s:%s' % (dep.dep_id,dep.dep_name))

# from sqlalchemy import or_,and_
#
# query11=session.query(Departments).filter(and_(Departments.dep_id>=1,Departments.dep_id<=4))
# print(query11)
# for dep in query11:
#     print('%s:%s' % (dep.dep_id,dep.dep_name))
#
# query11=session.query(Departments).filter(or_(Departments.dep_id<3,Departments.dep_id>5))
# print(query11)
# for dep in query11:
#     print('%s:%s' % (dep.dep_id,dep.dep_name))
# query13=session.query(Departments)
# print(query13.all())
# print(query13.first())


# query14=session.query(Departments.dep_name,Departments.dep_id).filter(Departments.dep_id==1)
# print(query14)
# print(query14.one())
# int primary key auto_increment first
#
# query15=session.query(Departments.dep_name,Departments.dep_id).filter(Departments.dep_id==1)
# print(query15)
# print(query15.scalar())

# query16=session.query(Departments).count()
# print(query16)

# query17=session.query(Employees.emp_name,Departments.dep_name).join(Departments)
# print(query17)
# for emp_name,dep_name in query17:
#     print('%s:%s' % (emp_name,dep_name))


# query18=session.query(Departments).filter(Departments.dep_name=='人力资源部')
# query18.one().dep_name='人力'

# print(hr)
# hr.dep_name='人力资源部'

query19=session.query(Departments).filter(Departments.dep_name=='行政部')
xz=query19.one()
print(xz)
session.delete(xz)

session.commit()
session.close