import sqlite3

class Author:
    _records = []

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Hizi ni gani umeanza") 
        self._name = value.strip()

    def save(self):
        conn = sqlite3.connect('Author.db')
        cursor = conn.cursor()

        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Author (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')

    
        if self.id is None:
            cursor.execute('INSERT INTO Author (name) VALUES (?)', (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE Author SET name = ? WHERE id = ?', (self.name, self.id))

        conn.commit()
        conn.close()

    @classmethod
    def find_id(cls,id):
        conn=sqlite3.connect('Author.db')
        cursor=conn.cursor()

        cursor.execute('SELECT id,name FROM Author WHERE id =?',(id,))
        row =cursor.fetchone()

        conn.close()
        if row:
            return cls(name=row[1] , id=row[0])
        else:
            return None
