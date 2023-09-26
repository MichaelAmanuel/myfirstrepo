import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     password='',
                                     database='sql_workbench')

        query = 'create table if not exists TakeoMySQLPythonConnect12JUL2023 (batch_id varchar(5),\
                student_id int,student_name varchar(255),student_qualification varchar(5),gender varchar(1),\
                email varchar(255),mobile varchar(20))'
        cur = self.con.cursor()
        cur.execute(query)
        # print('TakeoMySQLPythonConnect12JUL2023 - table create successfully ')

    def insert_record(self):
        query = 'insert into TakeoMySQLPythonConnect12JUL2023 values ("BDS29",1234,"Anand Shah","PG",\
                "M","anand.shah@papermail.com","987-7896-1234")'
        # print(query)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        # print('insert_record record inserted in TakeoMySQLPythonConnect12JUL2023 successfully')

    def insert_record_by_record(self, batch_id, student_id, student_name, student_qualification, gender, email, mobile):
        query = 'insert into TakeoMySQLPythonConnect12JUL2023 (batch_id,student_id,student_name,student_qualification,\
                    gender,email,mobile) values ({}, {}, {}, {}, {}, {}, {})'.format(batch_id, student_id,\
                        student_name, student_qualification, gender, email, mobile)
        # print(query)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        # print('insert_record_by_record record inserted in TakeoMySQLPythonConnect12JUL2023 successfully')

    # fetch all

    def fetch_all(self):
        query = "select * from TakeoMySQLPythonConnect12JUL2023"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("batch_id ", row[0])
            print("student_id ", row[1])
            print("student_name ", row[2])
            print("student_qualification ", row[3])
            print("gender ", row[4])
            print("email ", row[5])
            print("mobile ", row[6])
            print("#+++++ =========== +++++#")
            print("#+++++ Next Record +++++#")
            print("#+++++ VVVVVVVVVVV +++++#")

    # delete record

    def delete_record(self, student_id):
        query = 'delete from TakeoMySQLPythonConnect12JUL2023 where student_id= {}'.format(student_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('deleted student_id record {}'.format(student_id))


helper = DBHelper()
helper.insert_record()

helper.insert_record_by_record('"BDS29"', 1236, '"Amit Shah"', '"PG"', '"M"', '"amit.shah@papermail.com"',
                               '"987-7896-1236"')
helper.insert_record_by_record('"BDS29"', 1238, '"Maakhan Shah"', '"PG"', '"M"', '"maakhan.shah@papermail.com"',
                               '"987-7896-1238"')
helper.insert_record_by_record('"BDS29"', 1239, '"Jitu Shah"', '"PG"', '"M"', '"jitu.shah@papermail.com"',
                               '"987-7896-1239"')
helper.insert_record_by_record('"BDS29"', 1240, '"Hetal Shah"', '"PG"', '"F"', '"hetal.shah@papermail.com"',
                               '"987-7896-1240"')
helper.insert_record_by_record('"BDS29"', 1241, '"Shital Shah"', '"PG"', '"F"', '"shital.shah@papermail.com"',
                               '"987-7896-1241"')
helper.insert_record_by_record('"BDS29"', 2346, '"Amit Joshi"', '"PG"', '"M"', '"amit.joshi@papermail.com"',
                               '"987-7896-2346"')
helper.insert_record_by_record('"BDS29"', 2348, '"Maakhan Joshi"', '"PG"', '"M"', '"maakhan.joshi@papermail.com"',
                               '"987-7896-2348"')
helper.insert_record_by_record('"BDS29"', 2349, '"Jitu Joshi"', '"PG"', '"M"', '"jitu.joshi@papermail.com"',
                               '"987-7896-2349"')
helper.insert_record_by_record('"BDS29"', 2340, '"Hetal Joshi"', '"PG"', '"F"', '"hetal.joshi@papermail.com"',
                               '"987-7896-2340"')
helper.insert_record_by_record('"BDS29"', 2341, '"Shital Joshi"', '"PG"', '"F"', '"shital.joshi@papermail.com"',
                               '"987-7896-2341"')

helper.fetch_all()
helper.delete_record(1234)
