import pymysql

pymysql.install_as_MySQLdb()

class Connection:

    def __init__(self, user, password, db, host='localhost'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.use_unicode = True
        self.charset = "utf8"
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                use_unicode=self.use_unicode,
                charset=self.charset
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Picture:
    def __init__(self, db_connection, name, description):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO pictures (name, description) VALUES(%s, %s);", (self.name, self.description))

        self.db_connection.commit()
        c.close()


connection = Connection('root', '22121998', 'pic', 'localhost')
with connection:
    picture = Picture(connection,
                      'The Birth of Venus',
                      'Painting that depicts the emergence of Goddess Venus from the sea as a beautiful woman')
    picture.save()