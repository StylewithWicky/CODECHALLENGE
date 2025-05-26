import sqlite3

class Article:
    _records = []

    def __init__(self, name, title, magazine, author, id=None):
        self.name = name
        self.title = title
        self.magazine = magazine
        self.author = author
        self.id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value.strip()

    def save(self):
        conn = sqlite3.connect('Article.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Article (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                title TEXT NOT NULL,
                magazine TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')

        if self.id is None:
            cursor.execute(
                'INSERT INTO Article (name, title, magazine, author) VALUES (?, ?, ?, ?)',
                (self.name, self.title, self.magazine, self.author)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                'UPDATE Article SET name = ?, title = ?, magazine = ?, author = ? WHERE id = ?',
                (self.name, self.title, self.magazine, self.author, self.id)
            )

        conn.commit()
        conn.close()

    @classmethod
    def find_id(cls, id):
        conn = sqlite3.connect('Article.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id, name, title, magazine, author FROM Article WHERE id = ?', (id,))
        row = cursor.fetchone()

        conn.close()
        if row:
            return cls(id=row[0], name=row[1], title=row[2], magazine=row[3], author=row[4])
        return None

    @classmethod
    def find_title(cls, title):
        conn = sqlite3.connect('Article.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, title, magazine, author FROM Article WHERE title = ?', (title,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], title=row[2], magazine=row[3], author=row[4]) for row in rows]

    @classmethod
    def find_author(cls, author):
        conn = sqlite3.connect('Article.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, title, magazine, author FROM Article WHERE author = ?', (author,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], title=row[2], magazine=row[3], author=row[4]) for row in rows]
    @classmethod
    def find_magazine(cls, magazine):
        conn = sqlite3.connect('Article.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, title, magazine, author FROM Article WHERE magazine = ?', (magazine,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], title=row[2], magazine=row[3], author=row[4]) for row in rows]
