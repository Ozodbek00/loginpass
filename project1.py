
import mysql.connector


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

        user_input = """
        1. Registratsiya
        2.Login
        """
        while user_input not in ['1', '2']:
            user_input = """
        Xato!
        1. Registratsiya
        2.Login
        """
        if user_input == '1':
            self.register()

        else:
            self.login_()

    def register(self):
        pass

    def login_(self):
        pass

    def update_login(self):
        pass

    def update_pass(self):
        pass

    def log_out(self):
        pass

    def delete_acc(self):
        pass

