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
        query = "create table if not exists login_pass (id int unsigned auto_increment primary key, name varchar(20)\
         not null, login varchar not null, password varchar not null)"
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
        query = f"select login from login_pass where password={password_input}"
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
            self.update_pass(password_input)
        elif user_inp == '3':
            self.log_out()
        elif user_inp == '4':
            self.delete_acc()
        else:
            self.log_out()

    def login_(self):
        pass

    def update_login(self, old_log):
        pass

    def update_pass(self, old_pass):
        pass

    def log_out(self):
        pass

    def delete_acc(self):
        pass

