import psycopg2


class ConnectionDB:
    def __init__(self, login, password, database):
        self.connect = psycopg2.connect(
            user = login,
            password = password,
            database = database
        )
        self.cursor = self.connect.cursor()
    def get_data_speed(self):
        self.cursor.execute("select timestamp, speed from messages where terminal_id = '433427026902662' and timestamp > 1677618000 and timestamp < 1677704400")
        return  [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
    def get_calib_data(self):
        self.cursor.execute("select calibrating_data from clib where  deviceid_port like '433019520459465_%' limit 1")
        return  [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
    def close_db(self):
        self.cursor.close()
        self.connect.close()


