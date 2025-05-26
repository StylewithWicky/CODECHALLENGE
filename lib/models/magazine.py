import sqlite3

class Magazine:
    _records = []

    def __init__(self, name,category,id=None):
        self.name = name
        self.id = id
        self.category=category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Hizi ni gani umeanza") 
        self._name = value.strip()

    def save(self):
        conn = sqlite3.connect('Magazine.db')
        cursor = conn.cursor()

        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Magazine (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,category TEXT NOT NULL
            )
        ''')

    
        if self.id is None:
            cursor.execute('INSERT INTO Magazine (name,category) VALUES (?,?)', (self.name,self.category,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE Magazine SET name = ?,category =?  WHERE id = ?', (self.name,self.category, self.id))

        conn.commit()
        conn.close()

    @classmethod
    def find_id(cls,id):
        conn=sqlite3.connect('Magazine.db')
        cursor=conn.cursor()

        cursor.execute('SELECT id,name,category FROM Magazine WHERE id =?',(id,))
        row =cursor.fetchone()

        conn.close()
        if row:
            return cls(name=row[1] ,category=row[2], id=row[0])
        else:
            return None
        
    @classmethod 
    def find_name(cls,name):
        conn=sqlite3.connect('Magazine.db')
        cursor=conn.cursor()
        cursor.execute('SELECT id,name,category FROM Magazine WHERE name =?',(name,))
        rows =cursor.fetchall()
        conn.close()
        
        return [cls(id=row[0] ,name=row[1] ,category=row[2])for row in rows]
    
    @classmethod 
    def find_category(cls,category):
        conn=sqlite3.connect('Magazine.db')
        cursor=conn.cursor()
        cursor.execute('SELECT id,name,category FROM Magazine WHERE category =?',(category,))
        rows =cursor.fetchall()
        conn.close()
        
        return [cls( id=row[0] ,name=row[1] ,category=row[2]) for row in rows]
      
    
