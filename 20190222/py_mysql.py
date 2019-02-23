
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='nsd1809',
    charset='utf8'
)
cursor = conn.cursor()

# create_department="""create table department(dep_id int,dep_name varchar(20) not null unique,PRIMARY KEY(dep_id))
# """

# create_employees="""create table employees(emp_id int,emp_name varchar(20),
# gender varchar(6),birth_date date,email varchar(50),dep_id int,
# FOREIGN KEY (dep_id) REFERENCES department (dep_id))
# """


# create_salary="""create table salary(
# auto_id int auto_increment,emp_id int,date date,basic int,awards int,PRIMARY KEY(auto_id),
# FOREIGN KEY(emp_id) REFERENCES employees(emp_id))
# """

create_salary = """CREATE TABLE salary(
auto_id INT, emp_id INT, date DATE, basic INT, awards INT,
PRIMARY KEY(auto_id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)"""


# cursor.execute(create_department)
# cursor.execute(create_employees)
cursor.execute(create_salary)


conn.commit()
cursor.close()
conn.close()


