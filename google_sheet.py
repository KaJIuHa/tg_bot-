import sqlite3


class Database:
    __ins = None
    def __new__(cls, *args, **kwargs):
        if cls.__ins is None:
            cls.__ins = super().__new__(cls)
            return cls.__ins
        raise AttributeError("Невозможно создадть новый экземпляр класса Database")

    def __init__(self, db_name, password=None):
        self.db_name = db_name
        if password is not None:
            self.password = password

    def connect(self):
        return sqlite3.connect(self.db_name)




# conn = sqlite3.connect("tutorial.db")
# cur




if __name__ == "__main__":
    obj = Database("tutorial.db")
    db = obj.connect()
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS expanses(title, year, score)")
    # cur.execute("""
    # INSERT INTO expanses VALUES
    #              ('Monty Python and the Holy Grail', 1975, 8.2),
    #              ('And Now for Something Completely Different', 1971, 7.5),
    #              ('Alex', 1972, 7.8);
    #              """)
    # db.commit()
    val = cur.execute("""
    SELECT year, score
    FROM expanses
    WHERE score > 8
    """)
    print(val.fetchall())

#     12/12/2023    50 40 30
#     12/12/2023             300







