import os
import mysql.connector
import time

class Login:
    def initial_mes(self):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlok2002",
            database="w6"
        )

        mycursor = my_db.cursor()
        query = "create table if not exists login_pass (id int unsigned auto_increment primary key, \
        name varchar(20) not null, login varchar(12) not null, password varchar(12) not null)"
        mycursor.execute(query)
        my_db.commit()
        os.system('cls')
        user_input = input("""
        1. Registratsiya
        2.Login
        """).strip()
        while user_input not in ['1', '2']:
            user_input = input("""
        Xato!
        1. Registratsiya
        2.Login
        """).strip()
        if user_input == '1':
            self.register()

        else:
            self.login_()

    def register(self):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlok2002",
            database="w6"
        )

        mycursor = my_db.cursor()

        name_input = input("Ismingiz: ").strip()
        while not name_input:
            name_input = input("Xatolik! Ismingiz? ").strip()
        login_input = input("Login: ").strip()
        password_input = input("Parol: ").strip()
        query = f"select * from login_pass where login='{login_input}'"
        mycursor.execute(query)
        datas = mycursor.fetchall()
        while datas or not login_input or not password_input:
            os.system('cls')
            print("Xatolik! Login va password ni qayta kiriting: ")
            login_input = input().strip()
            password_input = input().strip()
        query = f'insert into login_pass (name, login, password)\
         values ("{name_input}", "{login_input}", "{password_input}")'
        mycursor.execute(query)
        my_db.commit()
        os.system('cls')
        user_inp = input(f"""
        Tabriklaymiz, {name_input} siz registratsiyadan o'tdingiz
        1. Update login
        2. Update password
        3. Log out
        4. Delete account
        """).strip()
        os.system('cls')
        if user_inp == '1':
            self.update_login(login_input)
        elif user_inp == '2':
            self.update_pass(login_input, password_input)
        elif user_inp == '3':
            self.log_out()
        elif user_inp == '4':
            self.delete_acc(login_input)
        else:
            self.log_out()

    def login_(self):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlok2002",
            database="w6"
        )

        mycursor = my_db.cursor()
        os.system('cls')
        user_log = input("Login: ").strip()
        user_pass = input("Password: ").strip()
        query = f"select password from login_pass where login='{user_log}'"
        mycursor.execute(query)
        datas = mycursor.fetchall()
        quitt = 5
        while not datas or not user_pass or not user_log or user_pass != datas[0][0]:
            user_log = input("Xato! Login: ").strip()
            user_pass = input("Password: ").strip()
            query = f"select password from login_pass where login='{user_log}'"
            mycursor.execute(query)
            datas = mycursor.fetchall()
            quitt -= 1
            if quitt == 0:
                print("Dang! Keyinroq harakat qilib ko'ring")
                time.sleep(3)
                quit()
        query = f"select name from login_pass where login='{user_log}'"
        mycursor.execute(query)
        datas = mycursor.fetchall()
        os.system('cls')
        user_inp = input(f"""
                Tabriklaymiz, {datas[0][0]} siz tizimdasiz
                1. Update login
                2. Update password
                3. Log out
                4. Delete account
                """).strip()
        os.system('cls')
        if user_inp == '1':
            self.update_login(user_log)
        elif user_inp == '2':
            self.update_pass(user_log, user_pass)
        elif user_inp == '3':
            self.log_out()
        elif user_inp == '4':
            self.delete_acc(user_log)
        else:
            self.log_out()

    def update_login(self, old_log):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlok2002",
            database="w6"
        )

        mycursor = my_db.cursor()
        os.system('cls')

        new_log = input("Yangi loginingizni kiriting: ").strip()
        query = f"select login from login_pass where login='{new_log}'"
        mycursor.execute(query)
        datas = mycursor.fetchall()
        while datas or not new_log:
            new_log = input("Yangi loginingizni kiriting: ").strip()
            query = f"select login from login_pass where login='{new_log}'"
            mycursor.execute(query)
            datas = mycursor.fetchall()
        query = f"update login_pass set login='{new_log}' where login='{old_log}'"
        mycursor.execute(query)
        my_db.commit()
        self.initial_mes()

    def update_pass(self, loggg, old_pass):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlok2002",
            database="w6"
        )

        mycursor = my_db.cursor()
        os.system('cls')
        new_pass = input("Yangi parol kiriting: ").strip()
        while not new_pass or new_pass == old_pass:
            new_pass = input("Yangi parol kiriting: ").strip()
        query = f"update login_pass set password ='{new_pass}' where login='{loggg}'"
        mycursor.execute(query)
        my_db.commit()
        os.system('cls')
        user_inp = input(f"""
                        Tabriklaymiz,  sizning parolingiz o'zgardi ****
                        1. Update login
                        2. Update password
                        3. Log out
                        4. Delete account
                        """).strip()
        os.system('cls')
        if user_inp == '1':
            self.update_login(loggg)
        elif user_inp == '2':
            self.update_pass(loggg, new_pass)
        elif user_inp == '3':
            self.log_out()
        elif user_inp == '4':
            self.delete_acc(loggg)
        else:
            self.log_out()

    def log_out(self):
        print("Salomat bo'ling")
        time.sleep(3)
        quit()

    def delete_acc(self, login):
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlok2002",
            database="w6"
        )

        mycursor = my_db.cursor()
        query = f"delete from login_pass where login='{login}'"
        mycursor.execute(query)
        my_db.commit()
        print("5 soniyadan keyin siz tizimdan chiqib ketasiz")
        time.sleep(5)


user = Login()
user.initial_mes()
