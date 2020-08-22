import sqlite3


class myconnect:

    def __init__(self):
        self.connection = sqlite3.connect("emp.db")
        self.connection.execute(''' create table if not exists emp(
                  id integer primary  key AUTOINCREMENT,
                  name text,
                  email text,
                  mobile_no text,
                  type text,
                  experience integer,
                  salary text
            ) ''')

    def savetodb(self, ename, eemail, emob, etype, eexp, esalary):
        # 6 Save To DB
        with self.connection:
            self.connection.execute(
                "insert into emp(name,email,mobile_no,type,experience,salary) values(:name,:email,:mobile_no,:type,:experience,:salary)",
                {'name': ename, 'email': eemail, 'mobile_no': emob, 'type': etype, 'experience': eexp,
                 'salary': esalary})
        self.connection.commit()

    def display(self):
        # 7 Display Info Of a Email
        eid = input("enter the emp id: ")
        with self.connection:
            dataEmp = self.connection.execute(
                'select id,name,email,mobile_no,type,experience,salary from emp where id=:id',
                {'id': eid})
            l = dataEmp.fetchall()
            print  ("=========================================================")
            print ("Employee Name : " + l[0][1])
            print ("Employee Email : " + l[0][2])
            print ("Employee Mobile No. : " + l[0][3])
            print ("Employee Type : " + l[0][4])
            print ("Employee Experience : ", l[0][5])
            print ("Employee Salary : ", l[0][6])
            print  ("=========================================================")
